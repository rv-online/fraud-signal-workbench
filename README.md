# Fraud Signal Workbench

Python analytics project for transaction risk triage. It packages a small but reviewable workflow with deterministic scoring, JSON outputs, and unit tests.

## What It Shows

- risk scoring, queue prioritization, and analyst-ready summaries
- clear ingestion and summarization logic
- CLI entrypoint and test coverage

## Run

```bash
python -m src.analyzer --input data/transactions.ndjson --output out/report.json
```

## Test

```bash
python -m unittest discover -s tests
```
