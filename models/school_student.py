# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

class SchoolStudent(models.Model):
    #Nombre y descripción del modelo
    _name = 'school.student'
    _description = 'Estudiante'

    #Campos del modelo
    name = fields.Char(string = 'Nombre', required = True)
    birth_date = fields.Date(string = 'Fecha de nacimiento')
    age = fields.Integer(string = 'Edad', compute = '_compute_age', store = True)
    final_exam_grade = fields.Float(string = 'Nota final de examen')

    #Campos relacionales 
    subjects_ids = fields.Many2many(
        'school.subject', string = 'Cursos matriculados', readonly = False)
    
    #Campos extras (sugerencias)
    nationality = fields.Char(string = 'Nacionalidad')
    email = fields.Char(string = 'Email')
    phone = fields.Char(string = 'Número de teléfono')
    addres = fields.Char(string = 'Dirección')
    enrollment_date = fields.Date(string = 'Fecha de inscripción')

    grade_level = fields.Selection(
        [('1', '1er Grado'),('2', '2do Grado'),('3', '3er Grado'),('4', '4to Grado'),('5', '5to Grado')], 
        string = 'Grado')

    gender = fields.Selection(
        [('m', 'Masculino'), ('f', 'Femenino'), ('O', 'Otros')], string = 'Género')

    years_enrolled = fields.Integer(string = 'Años inscritos', compute='_compute_years_enrolled', store = True)

    #Funcion para calcular edad (campo age)
    @api.depends('birth_date')
    def _compute_age(self):
        today = date.today()
        for student in self:
            if student.birth_date:
                birthdate = student.birth_date
                if ((today.month, today.day) > (birthdate.month, birthdate.day)):
                    student.age = today.year - birthdate.year - 1
                else:
                    student.age = today.year - birthdate.year
            else:
                student.age = 0
    
    #Funcion para calcular años inscritos (campo years_enrolled)
    @api.depends('enrollment_date')
    def _compute_years_enrolled(self):
        today = date.today()
        for student in self:
            if student.enrollment_date:
                enrollmentDate = student.enrollment_date
                if ((today.month, today.day) > (enrollmentDate.month, enrollmentDate.day)):
                    student.years_enrolled = today.year - enrollmentDate.year - 1
                else:
                    student.years_enrolled = today.year - enrollmentDate.year
            else:
                student.years_enrolled = 0

            
     