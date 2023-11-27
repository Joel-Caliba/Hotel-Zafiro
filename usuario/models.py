'''
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('El campo Email es obligatorio')
        usuario = self.model(
            username = username,
            email = self.normalize_email(email),
        )
        usuario.set_password(password)
        usuario.save()
        return usuario
    def create_superuser(self, username, email, password):

        usuario = self.create_user( 
            email,
            username=username, 
            password=password
            )
        
        usuario.usuario_administrador = True
        usuario.save()
        return usuario
class Usuario(AbstractBaseUser):
    username = models.CharField('Nombre de usuario', unique=True, max_length=15)
    email = models.EmailField("Correo Electronico", max_length=250, unique=True)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f'Usuario {self.username}, {self.email}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
#verifica si el usuaruio es administrador
    @property
    def is_staff(self):
        return self.usuario_administrador

'''