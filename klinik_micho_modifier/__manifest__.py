# -*- coding: utf-8 -*-
{
    'name': "klinik_micho_modifier",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence.xml',
        'views/klinik_pasien_views.xml',
        'views/klinik_dokter_views.xml',
        'views/klinik_administrasi_views.xml',
        'wizard/set_stok_obat_wizard.xml',
        'views/klinik_obat_views.xml',
        'views/klinik_resep_views.xml',
        'views/klinik_invoice_views.xml',
        'report/klinik_invoice_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
