from odoo import models, fields

class Apoderado(models.Model):
    _name = 'gestion_academica.apoderado'
    _description = 'Modelo para gestionar titulares'

    name = fields.Char(string='Nombre del titular', required=True)
    telefono = fields.Char(string='Telefono del titular', required=True)
    ci = fields.Char(string='CI del titular', required=True)
    parentesco_ids = fields.One2many('gestion_academica.parentesco', 'apoderado_id', string='Estudiantes')


