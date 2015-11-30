# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0002_document_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='filename',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
