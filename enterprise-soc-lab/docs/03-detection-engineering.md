# 03 - Detection engineering

## Detection 1: repeated failed authentication
- Signal: repeated authentication failures for one account on one endpoint.
- Starter threshold in the Python workbench: 3 or more failures per host/account in the supplied dataset.
- ATT&CK mapping: T1110 - Brute Force.
- False positives: mistyped passwords, stale service credentials, legitimate account lockout troubleshooting.
- Analyst pivots: source IP, target account, logon type, success after failures, endpoint owner, and time window.

## Detection 2: script interpreter process creation
- Signal: PowerShell or another script interpreter starts.
- ATT&CK lead: T1059 - Command and Scripting Interpreter (PowerShell sub-technique T1059.001).
- Important: process creation alone is not malicious. Review command line, parent process, user, script path, signer, and business context.

## Rule lifecycle
1. Define the behavior and data source.
2. Identify required fields and expected event volume.
3. Write a narrow rule.
4. Test against positive and benign examples.
5. Document false positives and ATT&CK mapping.
6. Tune severity only after validation.
7. Record rule version and test evidence.

The included Wazuh XML and Sigma examples are starter templates. Validate syntax, decoder/field compatibility, rule IDs, and version behavior in your own lab before enabling them.
