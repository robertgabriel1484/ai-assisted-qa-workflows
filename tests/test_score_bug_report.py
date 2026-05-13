import unittest
from pathlib import Path

from scripts.score_bug_report import score_bug_report


class ScoreBugReportTests(unittest.TestCase):
    def test_improved_bug_report_scores_high(self):
        result = score_bug_report(Path("sample_artifacts/sample_bug_report_after.md"))

        self.assertGreaterEqual(result["percentage"], 90)
        self.assertEqual(result["max_score"], 10)


if __name__ == "__main__":
    unittest.main()
