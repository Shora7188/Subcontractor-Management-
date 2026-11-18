# -*- coding: utf-8 -*-
{
    'name': 'Subcontract Management',
    'version': '17.0.1.0.0',
    'summary': 'Subcontract Contracts and Progress Invoices',
    'description': """
Subcontract Management for Odoo 17.

Features:
- Subcontract Management
- Contract BOQ Management
- Subcontract Progress Invoices
- Progress Quantities and Calculations
- Tax Calculation
- PDF Progress Invoice Reports
- Excel Import
- Contract and Invoice Attachments
- Purchase and Accounting Integration
    """,

    'author': 'Ashraf Shora',
    'website': 'https://github.com/Shora7188',
    'category': 'Accounting/Construction',

    'license': 'OPL-1',
    'price': 1200.00,
    'currency': 'USD',

    'support': 'ضع بريد الدعم الخاص بك هنا',

    'depends': [
        'base',
        'account',
        'product',
        'purchase',
    ],

    'data': [
        'security/subcontract_security.xml',
        'security/ir.model.access.csv',
        'wizard/add_qty_wizard_view.xml',
        'views/subcontract_views.xml',
        'views/subcontract_config_views.xml',
        'reports/progress_invoice_templates.xml',
        'reports/progress_invoice_report.xml',
        'views/subcontract_progress_invoice_views.xml',
        'views/subcontract_menu.xml',
        'data/sequence.xml',
        'wizard/import_contract_line_wizard.xml',
    ],

    'installable': True,
    'application': True,
}