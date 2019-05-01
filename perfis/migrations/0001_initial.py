# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=80)),
                ('sobrenome', models.CharField(max_length=80)),
                ('nome_empresa', models.CharField(max_length=80)),
                ('telefone', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=80)),
                ('senha', models.CharField(max_length=12)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
