# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='uid',
            field=models.CharField(max_length=40, default=uuid.uuid4),
        ),
    ]
