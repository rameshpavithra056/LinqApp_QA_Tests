# Bug Report - LinqApp `/welcome` Page

## Issue Summary
The social login buttons (`Email`, `Apple`, `Google`, `LinkedIn`) do not have `aria-label` attributes, affecting accessibility.

## Steps to Reproduce
1. Navigate to [staging-web.linqapp.com/welcome](https://staging-web.linqapp.com/welcome).
2. Inspect the social login buttons.
3. Observe missing `aria-label` attributes.

## Expected Behavior
Each button should have an `aria-label` for accessibility.

## Actual Behavior
No `aria-label` attributes are set on the buttons.

## Suggested Fix
Add `aria-label` attributes to improve screen reader support.
