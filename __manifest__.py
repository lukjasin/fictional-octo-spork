{
    "name": "Fictional Octo Spork",
    "version": "1.0",
    "website": "https://www.portacapena.com",
    "author": "Kimbo",
    "description": """
        Real estate ads module to show available properties.
    """,
    "category": "Sales",
    "depends": [],
    "data": [
        'security/ir.model.access.csv',
        'views/property_view.xml',
        'views/property_type_view.xml',
        'views/property_tag_view.xml',
        'views/menu_items.xml',
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3"
}