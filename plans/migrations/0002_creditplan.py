# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditPlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(editable=False, db_index=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='name')),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('credits', models.PositiveIntegerField(verbose_name='number of credits')),
                ('available', models.BooleanField(default=False, help_text='Is still available for purchase', db_index=True, verbose_name='available')),
                ('visible', models.BooleanField(default=True, help_text='Is visible in current offer', db_index=True, verbose_name='visible')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(max_digits=7, decimal_places=2, db_index=True)),
            ],
            options={
                'ordering': ('price',),
                'verbose_name': 'credit plan',
                'verbose_name_plural': 'credit plans',
            },
            bases=(models.Model,),
        ),
    ]
