# Generated by Django 3.0.5 on 2021-01-17 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MongoDB', '0008_file_filedetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='fieldcoor',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
