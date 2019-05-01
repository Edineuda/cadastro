from django.conf.urls import patterns, include, url
from perfis.views import index, exibir


urlpatterns = patterns('',
    url (r'^$', 'perfis.views.index', name='index'),
    url (r'^perfil/(?P<perfil_id>\d)+$', 'perfis.views.exibir', name='exibir')
)
