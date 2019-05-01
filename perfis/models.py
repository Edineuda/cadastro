from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):

		nome = models.CharField(max_length=80, null=False)
		sobrenome = models.CharField(max_length=80, null=False)
		nome_empresa = models.CharField(max_length=80, null=False)
		telefone = models.CharField(max_length=30, null=False)
		senha = models.CharField(max_length=12, null=False)
		confirmar_senha = models.CharField(max_length=12, null=False)

		contatos = models.ManyToManyField('self')

		usuario = models.OneToOneField(User, related_name="perfil")

		@property
		def email(self):
			return self.usuario.email
		

		
		
		