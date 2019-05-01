from django.conf.urls import patterns, url
from usuarios.views import CadastrarUsuario
from usuarios.forms import CadastrarUserForm

urlpatterns = patterns('',
	url(r'^cadastrar/$', CadastrarUsuario.as_view(), name="cadastrar")
)