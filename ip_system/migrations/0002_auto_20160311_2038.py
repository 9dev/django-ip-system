# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ip_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ip',
            name='address',
            field=models.GenericIPAddressField(db_index=True, unique=True),
        ),
    ]
