# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 19:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20171202_0046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['date_created'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.RenameField(
            model_name='commentpost',
            old_name='created',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='commentpost',
            old_name='moder',
            new_name='is_moderated',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='create',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='update',
            new_name='date_updated',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='moder',
            new_name='is_moderated',
        ),
    ]
