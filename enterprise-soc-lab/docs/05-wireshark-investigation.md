# 05 - Wireshark investigation

1. Capture only on your own isolated lab network or a network for which you have explicit permission.
2. Prefer a short capture around a controlled test.
3. Apply filters from `wireshark/display-filters.txt`.
4. Record source/destination, protocol, timestamps, and relevant packet numbers.
5. Correlate packet timestamps with endpoint alerts.
6. Export only sanitized screenshots or notes; do not commit raw PCAPs by default.

A display filter narrows what is shown; it does not prove malicious activity. Encrypted TLS payloads generally cannot be read as plaintext without appropriate authorized decryption context.
