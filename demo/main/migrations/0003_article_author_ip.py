# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ip_system', '0001_initial'),
        ('main', '0002_remove_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author_ip',
            field=models.ForeignKey(to='ip_system.Ip', null=True),
        ),
    ]
