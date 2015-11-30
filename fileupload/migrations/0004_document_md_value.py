# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0003_document_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='md_value',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
