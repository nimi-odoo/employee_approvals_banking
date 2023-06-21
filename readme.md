# Overview
---
This module restricts an employee from directly changing their banking information. Instead, the employee submits a request to update their information in Approvals, where it is reviewed by HR. If the request is approved, the employee's banking information is automatically updated.
This needs a new Approvals Type to be configured. The added "Bank Account" field should be set to "Required".

## Setup
1. Open the Approvals app and then set up a new Approvals Type by going to Configuration -> Approvals Types.
2. Select "New", set the "Bank Account" field to "Required" and specify approvers for this type.

## Example Workflow
1. The employee wants to update their banking info. On their profile, their banking info is displayed on the "Private Information" tab under "Bank Account Number" and is readonly.
2. To update it, the employee goes to the Approvals app and selects "New Request" for the approval type corresponding to updating bank information.
3. In the "Bank Info" field the user can specify an existing `res.partner.bank` record or create a new one. Submit when done.
4. The approval will appear for the approver on their approvals dashboard under "To Review" for the associated approval type.
5. The approver reviews the information and either approves or refuses.
6. If the request is approved, the new bank account will be visible from the employee's profile.
