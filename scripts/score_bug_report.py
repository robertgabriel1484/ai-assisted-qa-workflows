#!/usr/bin/env python3
"""Score a bug report for clarity and completeness."""

from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED_SECTIONS = [
    "title",
    "environment",
    "preconditions",
    "steps to reproduce",
    "expected result",
    "actual result",
    "severity",
    "priority",
    "impact",
    "evidence",
]


def score_bug_report(path: Path) -> dict[str, object]:
    content = path.read_text(encoding="utf-8").lower()
    missing: list[str] = []
    score = 0

    for section in REQUIRED_SECTIONS:
        if section in content:
            score += 1
        else:
            missing.append(section)

    max_score = len(REQUIRED_SECTIONS)

    return {
        "score": score,
        "max_score": max_score,
        "percentage": round((score / max_score) * 100, 2),
        "missing": missing,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Score a bug report for QA completeness.")
    parser.add_argument("bug_report_file", type=Path, help="Path to bug report markdown file.")
    args = parser.parse_args()

    result = score_bug_report(args.bug_report_file)

    print("Bug Report Score")
    print("----------------")
    print(f"Score: {result['score']}/{result['max_score']} ({result['percentage']}%)")

    if result["missing"]:
        print("\nMissing Sections")
        print("----------------")
        for item in result["missing"]:
            print(f"- {item}")


if __name__ == "__main__":
    main()
