# Generated by Django 2.1.3 on 2018-11-12 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='repo',
            field=models.FileField(upload_to='documents/'),
        ),
    ]
