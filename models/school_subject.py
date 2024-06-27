# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SchoolSubject(models.Model):
    #Nombre y descripción del modelo
    _name = 'school.subject'
    _description = 'Curso'  

    #Campos del modelo
    name = fields.Char(string = 'Nombre', required = True)
    credits = fields.Integer(string = '# de Créditos', required = True)
    max_students = fields.Integer(string = 'Estudiantes Máximos', required = True)
    active = fields.Boolean(string = 'Materia Activa', required = True)

    #Campos relacionales
    student_ids = fields.Many2many(
        'school.student', string = 'Estudiantes', readonly = False)
    
    teacher_id = fields.Many2one(
        'school.teacher', string = 'Profesor', readonly = False)
    
    #Campos extras (sugerencias)
    description = fields.Text(string = 'Descripción')
    schedule = fields.Text(string = 'Horario')
    classroom = fields.Char(string = 'Salón')

    class_modality = fields.Selection(
        [('p', 'Presencial'), ('v', 'Virtual'), ('h', 'Híbrida')], string = 'Modalidad')
    
    semester = fields.Selection(
        [('1', '2024-I'), ('2', '2024-II'), ('3', 'Verano')], string = 'Semestre')
    
    current_students = fields.Integer(string = 'Estudiantes actuales', compute = '_compute_current_students', store = True)
    remaining_slots = fields.Integer(string = 'Cupos disponibles', compute = '_compute_remaining_slots', store = True)

    #Función para calcular cuantos estudiantes están escritos en el curso (campo current_students)
    @api.depends('student_ids')
    def _compute_current_students(self):
        for subject in self:
            subject.current_students = len(subject.student_ids)
    
    #Función para calcular cuantos cupos quedan disponibles en el curso (campo remaining_slots)
    @api.depends('current_students', 'max_students')
    def _compute_remaining_slots(self):
        for subject in self:
            subject.remaining_slots = subject.max_students - subject.current_students

