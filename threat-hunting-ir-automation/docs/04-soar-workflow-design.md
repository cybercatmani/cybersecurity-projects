# SOAR workflow design - planned extension
Shuffle or another SOAR platform may orchestrate approved tasks. No live integration is included.

Proposed flow: receive validated alert -> normalize/deduplicate -> permitted enrichment -> create/update case -> analyst review -> explicit approval gate -> approved action -> audit record.

Start with notification and case creation only. Store tokens in the platform secret store, never Git. Use sandbox workflows, rate limits, error handling, audit logs, and a manual kill switch. Never isolate endpoints or block indicators from one unvalidated match.
