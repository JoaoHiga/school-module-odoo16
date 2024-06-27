# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

class SchoolTeacher(models.Model):
    #Nombre y descripción del modelo
    _name = 'school.teacher'
    _description = 'Profesor'  
     
    #Campos del modelo
    name = fields.Char(string = 'Nombre', required = True)
    profile = fields.Text(string = 'Perfil')

    #Campos relacionales
    subjects_ids = fields.One2many(
        'school.subject', 'teacher_id', string = 'Cursos', readonly = False)
    
    #Campos extras (sugerencias)
    nationality = fields.Char(string = 'Nacionalidad')
    email = fields.Char(string = 'Email')
    phone = fields.Char(string = 'Número de teléfono')
    addres = fields.Char(string = 'Dirección')
    hire_date  = fields.Date(string = 'Fecha de contratación')
    specialization = fields.Char(string = 'Especialización')
    years_of_service = fields.Integer(string = 'Años de servicio', compute = '_compute_years_of_service', store = True)
    birth_date = fields.Date(string = 'Fecha de nacimiento')
    age = fields.Integer(string = 'Edad', compute = '_compute_age', store = True)

    gender = fields.Selection(
        [('m', 'Masculino'), ('f', 'Femenino'), ('O', 'Otros')], string = 'Género')
    
    #Función para calcular años de servicio (campo year_of_service)
    @api.depends('hire_date')
    def _compute_years_of_service(self):
        today = date.today()
        for teacher in self:
            if teacher.hire_date:
                hireDate = teacher.hire_date
                if ((today.month, today.day) > (hireDate.month, hireDate.day)):
                    teacher.years_of_service = today.year - hireDate.year - 1
                else:
                    teacher.years_of_service = today.year - hireDate.year
            else:
                teacher.years_of_service = 0