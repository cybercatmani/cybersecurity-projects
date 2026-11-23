# Threat hunting methodology
1. Hypothesis: state the behavior and why it matters.
2. Data: identify telemetry and confirm availability.
3. Query: define search logic and time range.
4. Analysis: validate patterns and benign explanations.
5. Pivot: follow related users, hosts, processes, and network events.
6. Conclusion: state what evidence supports and what remains unknown.
7. Detection: convert validated behavior into tested logic with documented false positives.
See `config/hunt-hypotheses.yml` for starting ideas.
