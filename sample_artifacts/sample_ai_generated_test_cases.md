# Sample AI-Generated Test Cases

## Test Case 1

Title: Imported open invoice appears in payment dashboard
Preconditions: Source invoice exists with OPEN status.
Steps:
1. Import invoice data.
2. Open payment dashboard.
3. Search for invoice ID.
Expected Result: Invoice appears with correct vendor, amount, tax, gross amount, and OPEN status.
Type: Positive
Priority: High

## Test Case 2

Title: Paid invoice transforms to PAID status
Preconditions: Source invoice has matching paid payment record.
Steps:
1. Import invoice and payment data.
2. Open payment dashboard.
3. Search for paid invoice ID.
Expected Result: Invoice final status is PAID.
Type: Positive
Priority: High

## Test Case 3

Title: Missing invoice ID is rejected
Preconditions: Source file contains a row with blank invoice ID.
Steps:
1. Import source file.
2. Review import results.
Expected Result: Row is rejected and error is logged.
Type: Negative
Priority: High

## Test Case 4

Title: Dashboard total matches backend invoice total
Preconditions: Invoices are imported successfully.
Steps:
1. Sum gross amount from backend target table.
2. Compare against dashboard total.
Expected Result: Dashboard total matches backend total.
Type: Data Validation
Priority: High
