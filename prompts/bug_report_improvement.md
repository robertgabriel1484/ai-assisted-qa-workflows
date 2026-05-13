# Bug Report Improvement Prompt

Use this prompt to improve a vague bug report.

## Prompt

You are assisting a QA engineer improving a bug report.

Rewrite the bug report below so it is clear, reproducible, and useful for developers.

Bug report:

```text
PASTE BUG REPORT HERE
```

Include:

1. Clear title
2. Environment
3. Preconditions
4. Steps to reproduce
5. Expected result
6. Actual result
7. Severity
8. Priority
9. Impact
10. Evidence needed
11. Suggested root-cause area, if obvious
12. Follow-up questions

Return the answer in this format:

```text
Title:
Environment:
Preconditions:
Steps to Reproduce:
Expected Result:
Actual Result:
Severity:
Priority:
Impact:
Evidence:
Notes / Follow-Up:
```

## Human Review Notes

Do not invent evidence. If screenshots, logs, API responses, or SQL results are not available, mark them as needed.
