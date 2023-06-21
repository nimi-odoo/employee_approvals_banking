# -*- coding: utf-8 -*-
{
    'name': "Employee Payroll Information",
    'summary': """
        Validation for employee banking information
    """,
    'description': """
        This module restricts an employee from directly changing their banking information.
        Instead, the employee submits a request to update their information in Approvals,
        where it is reviewed by HR. If the request is approved, the employee's banking
        information is automatically updated.
        This needs a new Approvals Type to be configured. The added "Bank Account"
        field should be set to "Required".
    """,
    'author': "Odoo",
    'website': "https://www.odoo.com",
    'license': 'OPL-1',
    'application': False,
    'category': 'Approvals',
    'version': '0.1',
    'depends': ['hr', 'approvals', 'contacts'],
    'data': [
        'views/hr_employee_views.xml',
        'views/approval_category_views.xml',
        'views/approval_request_views.xml'
    ],
}
