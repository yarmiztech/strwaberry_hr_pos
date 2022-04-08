# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'K.S.A. - Point of Sale Branch',
    'author': 'Odoo S.A',
    'category': 'Accounting/Localizations/Point of Sale',
    'description': """
K.S.A. POS Localization
=======================================================
    """,
    'license': 'LGPL-3',
    'depends': ['l10n_gcc_pos', 'l10n_sa_invoice',"boraq_company_branches","base","point_of_sale"],
    'data': [
        # 'views/assets.xml',
        'views/point_of_sale.xml',
        'views/report_saledetails.xml',
    ],
    'qweb': [
        # 'static/src/xml/OrderReceipt.xml',
    ],
    'auto_install': True,
}
