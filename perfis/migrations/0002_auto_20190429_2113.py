# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('perfis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='email',
        ),
        migrations.AddField(
            model_name='perfil',
            name='confirmar_senha',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perfil',
            name='contatos',
            field=models.ManyToManyField(related_name='contatos_rel_+', to='perfis.Perfil'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='perfil',
            name='usuario',
            field=models.OneToOneField(related_name='perfil', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
