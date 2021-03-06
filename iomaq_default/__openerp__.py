# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
#
#    Copyright (C) 2016  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------------
{
    'name': 'Iomaq',
    'version': '9.0.1.2.0',
    'license': 'Other OSI approved licence',
    'category': 'Tools',
    'summary': 'Customización IOMAQ SA',
    'author': 'jeo Software',
    'depends': [
        'support_branding_jeosoft',

        # aplicaciones instaladas
        'sale', 'l10n_ar_aeroo_sale',  # ventas
        'purchase', 'l10n_ar_aeroo_purchase',  # compras
        'account_accountant',  # permisos para contabilidad
        'l10n_ar_aeroo_stock',

        'product_unique',
        'account_reconciliation_menu',  # agrega boton en partner
        'product_multi_barcode',
        'stock_picking_auto',  # Automatic picking when Invoice is validated.
        'price_security',  # Restringir quien ve el precio de costo
        'base_state_active',  # Deactivate US States
        'account_fix',  # Account Fixes
        'account_invoice_tax_wizard',  # add manual taxes on invoices
        'account_invoice_global_discount',  # descuentos en facturas de compra
        'web_export_view',  # exportar vistas en excel
    ],

    'data': [
        'views/product_view.xml',
        'views/afip_responsability.xml'
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],

    'port': '8069',
    'repos': [
        {'usr': 'jobiols', 'repo': 'cl-iomaq', 'branch': '9.0'},
        {'usr': 'jobiols', 'repo': 'odoo-addons', 'branch': '9.0'},
        {'usr': 'Vauxoo', 'repo': 'addons-vauxoo', 'branch': '9.0'},
        # {'usr': 'JayVora-SerpentCS',
        # 'repo':'SerpentCS_Contributions', 'branch': '9.0'},

    ],
    'docker': [
        {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
        {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '9.0'},
        {'name': 'postgres', 'usr': 'postgres', 'ver': '9.5'},
        {'name': 'nginx', 'usr': 'nginx', 'ver': 'latest'}
    ]
}
