# 05 — Optional network monitoring with Suricata

Suricata adds network IDS telemetry. Finish Windows → Wazuh first. Follow the official [Suricata installation guide](https://docs.suricata.io/en/latest/install.html).

## Install on Ubuntu sensor

```bash
sudo apt-get install -y software-properties-common
sudo add-apt-repository ppa:oisf/suricata-stable
sudo apt-get update
sudo apt-get install -y suricata jq
```

## Configure
Identify interfaces with `ip -br address`. Configure capture interface according to the installed version and your lab network. See the [official quickstart](https://docs.suricata.io/en/latest/quickstart.html).

Review `config/suricata/local.rules` and add it to the `rule-files` section of `/etc/suricata/suricata.yaml` (path can vary). The rule matches a literal HTTP URI `/soc-sentinel-demo` for a local test request only.

```bash
sudo suricata -T -c /etc/suricata/suricata.yaml
sudo systemctl restart suricata
sudo systemctl status suricata --no-pager
```

Generate a harmless request to a local HTTP server you control using that URI. Never scan or probe third-party systems.

## EVE JSON
Suricata commonly writes EVE JSON to `/var/log/suricata/eve.json`; confirm the configured path and inspect:

```bash
sudo tail -f /var/log/suricata/eve.json | jq .
```

To ingest it, configure a Wazuh agent on the sensor to monitor the JSON file (check current Wazuh JSON log collection guidance):

```xml
<localfile>
  <log_format>json</log_format>
  <location>/var/log/suricata/eve.json</location>
</localfile>
```

Restart the agent and verify events arrive before writing additional rules. A sensor cannot inspect traffic it never receives; NAT/host-only VMs may not see all physical-network traffic.
