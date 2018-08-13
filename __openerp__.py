{
    'name': "AES API",
    'version': '0.1',
    'depends': ['extraschool'],
    'author': "Imio",
    'website': "https://www.imio.be",
    'category': 'Api',
    'description': """
    API to communicate with AES through odoo's webservice. This is made to work with iA.Teleservice.
    """,
    # data files always loaded at installation
    'data': [
        'views/activity.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [

    ],
    'installable': True,
    'application': False,
}
