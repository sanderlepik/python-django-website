# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SecondIntroduction',
            new_name='Introductions',
        ),
        migrations.DeleteModel(
            name='FirstIntroduction',
        ),
    ]