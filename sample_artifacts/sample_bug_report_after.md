# Bug Report After

## Title

Payment dashboard total does not match backend invoice gross total after import

## Environment

- Application: Accounts Payable Platform
- Area: Invoice Import / Payment Dashboard
- Test Environment: QA
- Browser: Chrome

## Preconditions

- Source invoice file has been imported.
- Target invoice table contains transformed invoice records.
- Payment dashboard is available.

## Steps to Reproduce

1. Import the source invoice file.
2. Open the payment dashboard.
3. Capture the displayed total gross amount.
4. Run a backend SQL query to calculate `SUM(gross_amount)` from target invoices.
5. Compare dashboard total against backend total.

## Expected Result

Dashboard total gross amount matches backend `SUM(gross_amount)`.

## Actual Result

Dashboard total gross amount is different from the backend calculated total.

## Severity

High

## Priority

High

## Impact

Finance users may rely on incorrect payment totals, which can affect reconciliation, reporting, and payment review.

## Evidence

- Dashboard screenshot needed
- SQL query result needed
- Imported source file needed
- Test execution timestamp needed
