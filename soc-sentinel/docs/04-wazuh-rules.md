# 04 — Add the custom Wazuh detection rule

`config/wazuh/local_rules.xml` contains rule `100100`, a deliberately narrow match for the unique command-line marker produced by the included safe simulation.

## Install
On the Ubuntu Wazuh server, back up the current file:

```bash
sudo cp /var/ossec/etc/rules/local_rules.xml /var/ossec/etc/rules/local_rules.xml.backup.$(date +%F-%H%M%S)
```

Merge the repository's `<group>` block into `/var/ossec/etc/rules/local_rules.xml`; do not blindly overwrite existing rules. Keep one valid XML root. Validate:

```bash
sudo apt install -y libxml2-utils
sudo xmllint --noout /var/ossec/etc/rules/local_rules.xml
sudo systemctl restart wazuh-manager
sudo systemctl status wazuh-manager --no-pager
```

## Test
Run `Invoke-SafeSimulation.ps1` on Windows. Search Wazuh alerts for rule ID `100100` or description `SOC Sentinel safe simulation marker detected`.

## Explain the detection
- **Source:** Sysmon Operational event channel collected by Wazuh agent.
- **Event:** Sysmon process creation (Event ID 1).
- **Match:** command line contains the unique lab marker.
- **Level:** 5; a lab validation alert, not proof of compromise.
- **Triage:** verify process path, account, host, timestamp, parent process and whether it was approved activity.

This rule proves the pipeline works. It is not a general-purpose threat detector; production rules require representative testing, tuning, false-positive review and peer approval.
