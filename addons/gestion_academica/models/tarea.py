from odoo import models, fields

class Tarea(models.Model):
    _name = 'gestion_academica.tarea'
    _description = 'Tarea asignada a estudiantes'

    nombre = fields.Char(string="Nombre de la Tarea", required=True)
    descripcion = fields.Text(string="Descripción", required=True)
    fecha_entrega = fields.Date(string="Fecha de Entrega", required=True)
    curso_id = fields.Many2one('gestion_academica.curso', string="Curso", required=True)
    estudiante_ids = fields.Many2many('gestion_academica.estudiante', string="Asignada a Estudiantes")
    archivo_adjunto = fields.Binary(string="Archivo Adjunto")
    nombre_archivo = fields.Char(string="Nombre del Archivo")
    tipo_archivo = fields.Selection([
        ('imagen', 'Imagen'),
        ('audio', 'Audio'),
        ('pdf', 'PDF'),
        ('otro', 'Otro')
    ], string="Tipo de Archivo")
