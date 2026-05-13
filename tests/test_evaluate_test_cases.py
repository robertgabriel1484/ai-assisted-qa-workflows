import unittest
from pathlib import Path

from scripts.evaluate_test_cases import evaluate_test_cases


class EvaluateTestCasesTests(unittest.TestCase):
    def test_sample_test_cases_score_high(self):
        result = evaluate_test_cases(Path("sample_artifacts/sample_ai_generated_test_cases.md"))

        self.assertGreaterEqual(result["percentage"], 80)
        self.assertEqual(result["max_score"], 9)


if __name__ == "__main__":
    unittest.main()
