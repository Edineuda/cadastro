from django.conf.urls import patterns, url
from usuarios.views import CadastrarUsuario
from usuarios.forms import CadastrarUserForm

urlpatterns = patterns('',
	url(r'^cadastrar/$', CadastrarUsuario.as_view(), name="cadastrar"),
	url(r'^login/$', 'django.contrib.auth.views.login', {'template_name' : 'login.html'}, name='login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url' : '/login/' }, name='logout')
)