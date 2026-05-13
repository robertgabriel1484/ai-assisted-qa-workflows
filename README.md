# AI-Assisted QA Workflows

A QA/SDET portfolio project demonstrating practical, responsible AI-assisted QA workflows for test design, requirement clarification, edge-case discovery, bug report improvement, regression planning, and lightweight evaluation of AI-generated QA output.

## Project Purpose

This project demonstrates:

- AI-assisted test case generation
- Prompt libraries for QA workflows
- Requirement clarification prompts
- Edge-case discovery prompts
- Bug report improvement prompts
- Regression planning prompts
- Human review checklists
- Lightweight evaluation scoring
- Responsible AI usage in QA
- Python scripts for evaluating QA artifacts
- GitHub Actions CI execution

## Why This Matters

AI tools can help QA teams move faster, but human review is still required. This project shows how AI can support QA work without replacing judgment, product context, risk analysis, or final validation.

## Repository Structure

```text
ai-assisted-qa-workflows/
  docs/
    ai_qa_usage_guidelines.md
    human_review_checklist.md
    sample_before_after_bug_report.md
  prompts/
    bug_report_improvement.md
    edge_case_discovery.md
    regression_planning.md
    requirement_clarification.md
    test_case_generation.md
  sample_artifacts/
    sample_requirement.md
    sample_ai_generated_test_cases.md
    sample_bug_report_before.md
    sample_bug_report_after.md
  scripts/
    evaluate_test_cases.py
    score_bug_report.py
  tests/
    test_evaluate_test_cases.py
    test_score_bug_report.py
  README.md
  portfolio_project_log.md
```

## Included Workflows

### Requirement Clarification

Prompt patterns for identifying unclear requirements, missing acceptance criteria, dependencies, and testability risks.

### Test Case Generation

Prompt patterns for turning requirements into structured positive, negative, boundary, and regression test cases.

### Edge-Case Discovery

Prompt patterns for finding workflow gaps, invalid inputs, state transitions, data issues, and integration risks.

### Bug Report Improvement

Prompt patterns for improving issue reports with clear steps, expected/actual results, severity, priority, evidence, and impact.

### Regression Planning

Prompt patterns for building targeted regression plans based on changed functionality, defect history, and risk.

## Python Utilities

Run the test case evaluator:

```bash
python scripts/evaluate_test_cases.py sample_artifacts/sample_ai_generated_test_cases.md
```

Run the bug report scorer:

```bash
python scripts/score_bug_report.py sample_artifacts/sample_bug_report_after.md
```

Run unit tests:

```bash
python -m unittest discover tests
```

## CI/CD

This project is designed to run through GitHub Actions using:

```text
.github/workflows/ai-qa-workflow-tests.yml
```

## Portfolio Notes

My production QA background includes test planning, defect analysis, root-cause investigation, regression reporting, API testing, SQL validation, release readiness, and AI-assisted QA workflows.

This repo demonstrates how I use AI responsibly to support QA planning, documentation, test design, and analysis while keeping human review in control.
