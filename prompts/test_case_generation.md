# Test Case Generation Prompt

Use this prompt to turn a requirement into structured test scenarios.

## Prompt

You are assisting a QA engineer creating test cases.

Based on the requirement below, generate test cases covering:

1. Positive scenarios
2. Negative scenarios
3. Boundary cases
4. Data validation cases
5. API or integration cases, if applicable
6. Regression risks
7. Accessibility or usability considerations, if applicable
8. Assumptions and open questions

Requirement:

```text
PASTE REQUIREMENT HERE
```

Return test cases in this format:

```text
Test Case ID:
Title:
Preconditions:
Test Data:
Steps:
Expected Result:
Type: Positive / Negative / Boundary / Regression / API / Data
Priority:
Notes:
```

## Human Review Notes

Review each test case for accuracy, feasibility, duplication, and alignment with actual product behavior.
