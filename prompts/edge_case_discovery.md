# Edge-Case Discovery Prompt

Use this prompt to identify missed testing scenarios.

## Prompt

You are assisting a QA engineer with edge-case discovery.

Review the workflow below and identify edge cases related to:

1. Invalid inputs
2. Missing data
3. Duplicate data
4. State transitions
5. Permission or role issues
6. API failures
7. Slow responses or timeouts
8. Data reconciliation issues
9. Browser/device behavior
10. User interruption or repeated actions

Workflow:

```text
PASTE WORKFLOW HERE
```

Return the answer in this format:

```text
High-Risk Edge Cases:
Data Edge Cases:
API / Integration Edge Cases:
UI / Workflow Edge Cases:
Regression Risks:
Recommended Test Scenarios:
```

## Human Review Notes

Use AI output as a brainstorming aid. Prioritize edge cases based on business risk, defect history, and release scope.
