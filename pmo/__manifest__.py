# -*- coding: utf-8 -*-
#information from here: https://github.com/odoomates/Development-Tutorials/tree/12.0/om_hospital

{
    'name': "pmo",
    'version': '0.1',
    'category': 'Extra Tools',
    'summary': 'Module for managing pmo',
    'sequence': '10',
    'license': 'AGPL-3',
    'author': 'Felix',
    'maintainer': 'Felix',
    'website': 'www.google.de',
    'depends': ['account'],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'views/sprint.xml',
        'views/sequence.xml',
        'views/capacity.xml',
        'views/overall.xml',
        'views/overalltable.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False

}
