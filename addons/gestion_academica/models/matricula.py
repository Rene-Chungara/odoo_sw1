from odoo import models, fields

class Matricula(models.Model):
    _name = 'gestion_academica.matricula'
    _description = 'Modelo para gestionar matrículas'

    pagada = fields.Selection(
        [('pagada', 'pagada'),
        ('impaga', 'impaga'),],
        string='Estado',
        required=True
    )

    monto = fields.Float(string="Monto", required=True)
    subgestion_id = fields.Many2one('gestion_academica.subgestion', string='Subgestion', required=True, ondelete='cascade')
    gestion_id = fields.Many2one(related='subgestion_id.gestion_id', string='Gestión', readonly=True)
    estudiante_id = fields.Many2one('gestion_academica.estudiante', string='Estudiante', required=True, ondelete='cascade')

    @api.model
        def calcular_total_pagado(self, fecha_inicio, fecha_fin):
            matriculas = self.search([
                ('create_date', '>=', fecha_inicio),
                ('create_date', '<=', fecha_fin),
                ('pagada', '=', 'pagada')
            ])
            total_pagado = sum(matriculas.mapped('monto'))
            return total_pagado