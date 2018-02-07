# -*- coding: utf-8 -*-
{
    'name': "Pupils on practices",
    
    'summary': """
        """,

    'description': """
        This is a module that helps the teachers to have a closer contact with 
        the activities their pupils are performing during their practices, as well
        as helps the pupils to have a summary of their activities.
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/users.xml',
        'views/pupilsop.xml',
        'views/partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}