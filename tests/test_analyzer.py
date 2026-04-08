import json
import unittest
from pathlib import Path

from src.analyzer import build_report, run


class AnalyzerTests(unittest.TestCase):
    def test_build_report_counts_records(self) -> None:
        report = build_report([
            {"transaction_id": "t_901", "merchant": "fast-cabs", "amount": 44, "risk_score": 0.11},
            {"transaction_id": "t_902", "merchant": "lux-travel", "amount": 910, "risk_score": 0.83},
        ])
        self.assertEqual(report["record_count"], 2)

    def test_run_writes_output(self) -> None:
        output_path = Path("out/test-report.json")
        report = run(Path("data/transactions.ndjson"), output_path)
        on_disk = json.loads(output_path.read_text(encoding="utf-8"))
        self.assertEqual(report["record_count"], 4)
        self.assertIn("risk_buckets", on_disk)


if __name__ == "__main__":
    unittest.main()
