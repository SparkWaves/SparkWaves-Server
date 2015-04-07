# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_lesson_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='description',
        ),
    ]
