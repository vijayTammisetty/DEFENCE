# Generated by Django 4.1.2 on 2022-11-05 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0010_rename_receiver_id_send_request_files_receiver_id1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='send_request_files',
            name='receiver_id1',
        ),
        migrations.RemoveField(
            model_name='send_request_files',
            name='sender_id1',
        ),
    ]