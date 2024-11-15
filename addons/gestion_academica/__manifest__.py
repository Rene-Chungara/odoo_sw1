{
    "name": "Gestión Académica",
    "version": "1.0",
    "summary": "Módulo para la gestión académica",
    "description": "Este módulo permite gestionar estudiantes, cursos y profesores.",
    "author": "Grupo 14 Sw",
    "category": "Education",
    "depends": ["contacts"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/estudiante_views.xml",
        "views/profesor_views.xml",
        "views/materia_views.xml",
        "views/curso_views.xml",
        "views/paralelo_views.xml",
        "views/sucursal_views.xml",
        "views/gestion_views.xml",
        "views/bloque_views.xml",
        "views/apoderado_views.xml",
        "views/horario_views.xml",
        "views/inscripcion_views.xml",
        "views/gestion_paralelo_views.xml",
        "views/tarea_view.xml",
        "menu/ga_menu.xml",
        "data/initial_data.xml",
        "data/data.xml",
    ],
    "installable": True,
    "application": True,
}
