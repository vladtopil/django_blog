# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('text', models.CharField(max_length=1500, verbose_name='Текст статьи')),
                ('image', models.ImageField(blank=True, upload_to='post/', verbose_name='Изображение')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('moder', models.BooleanField(default=False, verbose_name='Модерация')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'db_table': 'post',
                'ordering': ['create'],
            },
        ),
    ]