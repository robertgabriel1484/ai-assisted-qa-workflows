# Regression Planning Prompt

Use this prompt to build a targeted regression plan after a code change or defect fix.

## Prompt

You are assisting a QA engineer planning regression coverage.

Change summary:

```text
PASTE CHANGE SUMMARY HERE
```

Known impacted areas:

```text
PASTE IMPACTED AREAS HERE
```

Create a targeted regression plan including:

1. Smoke tests
2. Functional tests
3. Negative tests
4. API/integration checks
5. Data validation checks
6. Cross-browser or device checks
7. High-risk adjacent workflows
8. Defect re-test steps
9. Release-readiness risks
10. Go/No-Go considerations

Return the answer in this format:

```text
Regression Scope:
Smoke Coverage:
Functional Coverage:
API / Integration Coverage:
Data Validation Coverage:
High-Risk Areas:
Defect Re-Test Steps:
Go / No-Go Risks:
```

## Human Review Notes

Confirm scope with release notes, changed files, defect history, and Product/Engineering input.
