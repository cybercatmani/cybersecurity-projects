# YARA and IOC analysis
The supplied YARA rule matches a unique harmless marker in `sample-data/fixtures/training-note.txt`. It demonstrates syntax only; it is not malware detection.

After installing YARA, run:
```powershell
yara rules/training-indicator.yar sample-data/fixtures/training-note.txt
```

The IOC list contains documentation-only reserved examples. The default Python workflow is offline and does not call VirusTotal. Any future API enrichment must be authorized, use secure secret storage, and follow provider terms. Never upload confidential files or data without permission.
