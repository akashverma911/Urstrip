# Generated by Django 4.1.7 on 2023-05-05 17:56

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_mymodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='image_url',
            field=models.FileField(blank=True, null=True, upload_to=api.models.upload_to),
        ),
    ]
