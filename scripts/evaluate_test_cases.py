#!/usr/bin/env python3
"""Lightweight evaluator for AI-generated QA test cases."""

from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED_TERMS = [
    "title",
    "preconditions",
    "steps",
    "expected result",
    "type",
    "priority",
]


def evaluate_test_cases(path: Path) -> dict[str, object]:
    content = path.read_text(encoding="utf-8").lower()
    score = 0
    findings: list[str] = []

    for term in REQUIRED_TERMS:
        if term in content:
            score += 1
        else:
            findings.append(f"Missing recommended field: {term}")

    has_negative = "negative" in content
    has_positive = "positive" in content
    has_data_validation = "data validation" in content or "data" in content

    if has_positive:
        score += 1
    else:
        findings.append("Missing positive test coverage.")

    if has_negative:
        score += 1
    else:
        findings.append("Missing negative test coverage.")

    if has_data_validation:
        score += 1
    else:
        findings.append("Missing data validation coverage.")

    max_score = len(REQUIRED_TERMS) + 3

    return {
        "score": score,
        "max_score": max_score,
        "percentage": round((score / max_score) * 100, 2),
        "findings": findings,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate AI-generated test cases for basic QA completeness.")
    parser.add_argument("test_case_file", type=Path, help="Path to test case markdown file.")
    args = parser.parse_args()

    result = evaluate_test_cases(args.test_case_file)

    print("AI Test Case Evaluation")
    print("-----------------------")
    print(f"Score: {result['score']}/{result['max_score']} ({result['percentage']}%)")

    if result["findings"]:
        print("\nFindings")
        print("--------")
        for finding in result["findings"]:
            print(f"- {finding}")


if __name__ == "__main__":
    main()
