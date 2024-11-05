
{
    'name': 'Appeul Visa Management 1.0.0',
    'version': '17.0.1.0.0',
    'summary': 'Appeul Visa Management',
    'description': """Appeul Visa Management""",
    'author': 'Appeul Services',
    'company': 'Appeul',
    'maintainer': 'Appeul Services',
    'category': 'Sales',
    'website': 'https://www.appeul.com',
    'sequence':"-1110",
    'depends': ['base','ap_recruitment'],
    'data': [
        'security/ir.model.access.csv',
        # 'data/sequence.xml',
        # 'wizard/statement_wizard.xml',
        'views/visa.xml',
        'views/slot.xml',
        'views/view_applicants.xml',
        # 'report/im30.xml',
        # 'report/report.xml',
    ],

    # 'assets': {
    #         'web.assets_backend': [
    #             'ap_recruitment/static/src/components/**/*.js',
    #             'ap_recruitment/static/src/components/**/*.xml',
    #             'ap_recruitment/static/src/components/**/*.scss',
    #         ]
    #     },

    'installable': True,
    'application': True,


    'license': 'LGPL-3',

}
