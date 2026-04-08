# Fraud Signal Workbench

Python risk-scoring project for shaping transaction signals into analyst-facing fraud summaries.

## Why This Exists

Built to resemble the first pass of a fraud analytics system where investigators need interpretable signals rather than black-box outputs.

## What This Demonstrates

- signal extraction and risk-weighted summaries
- analyst-friendly outputs instead of notebook-only exploration
- clear, testable scoring logic

## Architecture

1. raw events are normalized into transaction-level signals
1. scoring logic aggregates risk factors into interpretable outputs
1. summaries are emitted for fraud review or downstream triage

## Run It

```bash
python -m unittest
```

## Verification

Use `python -m unittest` to confirm scoring rules and output generation.
