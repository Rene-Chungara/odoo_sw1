from odoo import models, fields

class Piso(models.Model):
    _name = 'gestion_academica.piso'
    _description = 'Modelo para gestionar pisos'

    name = fields.Char(string='Periodo', required=True)
    bloque_id = fields.Many2one('gestion_academica.bloque', string='Bloque', required=True)
