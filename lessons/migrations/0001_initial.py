# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000, null=True, blank=True)),
                ('overview', models.CharField(max_length=10000, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LessonProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('description', models.CharField(max_length=1000, null=True, blank=True)),
                ('image', models.URLField(null=True, blank=True)),
                ('lesson', models.ForeignKey(related_name='projects', to='lessons.Lesson')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LessonResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('resourceType', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('description', models.CharField(max_length=1000, null=True, blank=True)),
                ('image', models.URLField(null=True, blank=True)),
                ('lesson', models.ForeignKey(related_name='resources', to='lessons.Lesson')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
