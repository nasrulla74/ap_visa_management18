
{
    'name': 'Appeul Visa Management 1.0.1',
    'version': '18.0.1.0.1',
    'summary': 'Appeul Visa Management',
    'description': """Appeul Visa Management""",
    'author': 'Appeul Services',
    'company': 'Appeul',
    'maintainer': 'Appeul Services',
    'category': 'Sales',
    'website': 'https://www.appeul.com',
    'sequence':"-1110",
    'depends': ['base','ap_recruitment18'],
    'data': [
        'security/ir.model.access.csv',
        'views/visa.xml',
        'views/slot.xml',
        'views/view_applicants.xml',

    ],

    'installable': True,
    'application': True,


    'license': 'LGPL-3',

}
