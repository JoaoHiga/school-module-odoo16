# -*- coding: utf-8 -*-
{
    'name': "School",

    'summary':"""
        Sistema de gestión de colegio.
    """,

    'description': """
        Permite gestionar aulas de colegio, alumnos, profesores y cursos.
    """,

    'author': "Joao Higa",
    'website': "https://github.com/JoaoHiga",

    'category': 'Education',
    'version': '1.0.0',

    'depends': [
        'base',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/menu_item_views.xml',
        'views/school_subject_view.xml',
        'views/school_teacher_view.xml',
        'views/school_student_view.xml',
    ],

    'application': True,
    'installable': True,
    'auto_install': False,
    
    'license': 'LGPL-3'
}
