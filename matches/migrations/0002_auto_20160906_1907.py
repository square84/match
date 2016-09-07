# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='question_answered',
            new_name='questions_answered',
        ),
    ]
