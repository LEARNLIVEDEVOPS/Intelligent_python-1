# Generated by Django 3.0.5 on 2020-12-19 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MongoDB', '0002_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]