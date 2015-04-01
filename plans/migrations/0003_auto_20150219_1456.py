# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0002_creditplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='credit_plan',
            field=models.ForeignKey(related_name='plan_order', verbose_name='credit plan', blank=True, to='plans.CreditPlan', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='plan',
            field=models.ForeignKey(related_name='plan_order', verbose_name='plan', blank=True, to='plans.Plan', null=True),
            preserve_default=True,
        ),
    ]
