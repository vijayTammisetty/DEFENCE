# Generated by Django 4.1.1 on 2022-11-12 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0016_remove_request_recordmodel_request_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request_recordmodel',
            name='file',
        ),
    ]
