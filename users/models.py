from django.db import models
from django.contrib.auth.models import AbstractUser

# Definimos las opciones de ROLES
ROLE_CHOICES = (
    ('ADMIN', 'Administrador'),
    ('EDITOR', 'Editor'),
    ('CONSULTA', 'Consulta'),
)

class CustomUser(AbstractUser):
    # El campo de Rol
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='CONSULTA',
        verbose_name="Rol de Usuario"
    )

    # El campo de status (ya incluido en AbstractUser como is_active, pero lo mantenemos visible)
    # is_active = models.BooleanField(default=True) 

    class Meta:
        verbose_name = 'Usuario Modular'
        verbose_name_plural = 'Usuarios Modulares'

    def __str__(self):
        return self.username