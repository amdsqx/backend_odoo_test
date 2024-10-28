# -*- coding: utf-8 -*-
{
    'name': "backend_odoo_test",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base','point_of_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/materials.xml',
        'views/suppliers.xml',
        # 'views/assets.xml',
        # 'static/src/xml/visible_price_btn.xml',
    ],
    # 'assets': {
    #     'point_of_sale.assets': [
    #         'pos_disable_price/static/src/js/visible_price_btn.js',
    #         'pos_disable_price/static/src/xml/visible_price_btn.xml',
    #     ],
    # },

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application' : True,
    'auto_intstall' : False,
}
