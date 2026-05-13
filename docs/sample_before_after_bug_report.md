# Before and After Bug Report Example

## Before

```text
Invoice total is wrong on dashboard.

It happens after import. Please fix.
```

## After

```text
Title:
Payment dashboard total does not match backend invoice gross total after import.

Steps:
1. Import the source invoice file.
2. Open the payment dashboard.
3. Capture the displayed total gross amount.
4. Run backend SQL query to calculate SUM(gross_amount).
5. Compare dashboard total against backend total.

Expected:
Dashboard total matches backend total.

Actual:
Dashboard total differs from backend calculated total.

Impact:
Finance users may rely on incorrect totals during reconciliation and payment review.

Evidence Needed:
Dashboard screenshot, SQL query result, source file, test execution timestamp.
```

## QA Value

The improved report gives developers enough information to reproduce, investigate, and verify the issue.
