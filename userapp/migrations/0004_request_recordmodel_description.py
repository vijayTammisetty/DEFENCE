# Generated by Django 4.1.2 on 2022-11-03 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_request_recordmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='request_recordmodel',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
