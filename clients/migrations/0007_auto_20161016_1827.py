# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-16 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_auto_20161016_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='experience',
            field=models.IntegerField(choices=[(None, ''), (1, 'Nie gram w gry'), (2, 'Gram bardzo rzadko'), (3, 'Gram raz w tygodniu'), (4, 'Gram kilka razy w tygodniu'), (5, 'Gram codziennie')], default=3),
        ),
        migrations.AlterField(
            model_name='survey',
            name='satisfaction_level',
            field=models.IntegerField(choices=[(None, ''), (1, 'Było okropnie'), (2, 'Nie podobało mi się'), (3, 'Nic specjalnego'), (4, 'Było ok'), (5, 'Było fantastycznie')], default=3),
        ),
    ]
