# Generated by Django 4.1.2 on 2022-11-09 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0014_alter_send_request_files_receiver_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='request_recordmodel',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='qrimges/'),
        ),
    ]
