from odoo import models, fields, api

class Estudiante(models.Model):
    _name = 'gestion_academica.estudiante'
    _description = 'Modelo para gestionar estudiantes'

    name = fields.Char(string='Nombre', required=True)
    correo = fields.Char(string='Correo', required=True)  # Aseguramos que el correo sea obligatorio
    genero = fields.Selection(
        [('male', 'Masculino'), ('female', 'Femenino'), ('other', 'Otro')],
        string='Género'
    )
    direccion = fields.Char(string='Dirección')
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    telefono = fields.Char(string='Teléfono', required=True)  # Aseguramos que el teléfono sea obligatorio
    parentesco_ids = fields.One2many('gestion_academica.parentesco', 'estudiante_id', string='Tutor')
    matricula_ids = fields.One2many('gestion_academica.matricula', 'estudiante_id', string='Pagos')
    nota_ids = fields.One2many('gestion_academica.nota', 'estudiante_id', string='Notas')
    
    # Nuevo campo para asociar el estudiante a un usuario de Odoo
    user_id = fields.Many2one('res.users', string="Usuario relacionado")

    @api.model
    def create(self, vals):
        # Crear el registro del estudiante sin el usuario
        estudiante = super(Estudiante, self).create(vals)

        # Verificar que el teléfono esté disponible como contraseña
        contrasena = vals.get('telefono')
        if not contrasena:
            raise ValueError("El número de teléfono es obligatorio para crear el usuario.")

        # Verificar que el correo esté disponible como login
        correo = vals.get('correo')
        if not correo:
            raise ValueError("El correo electrónico es obligatorio para crear el usuario.")

        # Crear el usuario de Odoo usando el correo como login y el teléfono como contraseña
        usuario = self.env['res.users'].create({
            'name': estudiante.name,
            'login': correo,            # Usar el correo como login
            'password': contrasena,     # Usar el teléfono como contraseña
            'groups_id': [(4, self.env.ref('gestion_academica.group_gestion_academica_alumno').id),
            (4, self.env.ref('base.group_portal').id) 
            ],  # Ajusta el grupo según tu módulo
        })

        # Asignar el usuario al estudiante
        estudiante.user_id = usuario.id

        return estudiante
