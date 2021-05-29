# Generated by Django 3.0.5 on 2021-01-26 12:21

import MongoDB.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MongoDB', '0009_field_fieldcoor'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtractFIle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('file', models.FileField(blank=True, null=True, upload_to=MongoDB.models.ExtractFIle.directory)),
                ('modelname', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
