from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Tarea(models.Model):
    _name = 'gestion_academica.tarea'
    _description = 'Tarea asignada a estudiantes'
    _inherit = ['mail.thread']  # Agrega mail.thread para que soporte mensajes

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
    
    # Nuevo campo tipo
    tipo = fields.Selection([
        ('comunicado', 'Comunicado'),
        ('tarea', 'Tarea'),
        ('anuncio', 'Anuncio')
    ], string="Tipo", required=True, default='tarea')

    @api.model
    def create(self, vals):
        # Llamada al método original para crear la tarea
        tarea = super(Tarea, self).create(vals)

        # Notificación a los estudiantes asignados
        tarea._enviar_notificacion()

        return tarea

    def _enviar_notificacion(self):
        # Mensaje de notificación
        mensaje = _(
            "Se ha asignado una nueva actividad: %s\nDescripción: %s\nFecha de entrega: %s" % (
                self.nombre,
                self.descripcion,
                self.fecha_entrega,
            )
        )
        
        # Obtener los estudiantes asignados para enviar notificación
        usuarios_notificados = self.estudiante_ids.mapped('user_id').filtered(lambda u: u.active)

        # Enviar mensaje de notificación en la aplicación
        self.message_post(
            body=mensaje,
            subject="Nueva actividad asignada: %s" % self.nombre,
            message_type="notification",
            partner_ids=usuarios_notificados.mapped('partner_id').ids,
        )

        # Enviar correo de notificación
        for usuario in usuarios_notificados:
            # Configuración del correo
            mail_values = {
                'subject': "Nueva actividad asignada: %s" % self.nombre,
                'body_html': """
                    <p>Se ha asignado una nueva actividad:</p>
                    <p><strong>Nombre:</strong> {}</p>
                    <p><strong>Descripción:</strong> {}</p>
                    <p><strong>Fecha de entrega:</strong> {}</p>
                """.format(self.nombre, self.descripcion, self.fecha_entrega),
                'email_to': usuario.partner_id.email,  # Asegúrate de que el estudiante tenga un correo
                'email_from': self.env.user.partner_id.email or 'noreply@example.com',
            }

            # Crear y enviar el correo
            mail = self.env['mail.mail'].create(mail_values)
            mail.send()

