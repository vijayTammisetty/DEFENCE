# Generated by Django 4.1.2 on 2022-11-05 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0012_send_request_files_receiver_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='request_recordmodel',
            name='file',
            field=models.FileField(null=True, upload_to='from_receiver/'),
        ),
        migrations.AlterField(
            model_name='send_request_files',
            name='receiver_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver_id1', to='userapp.request_recordmodel'),
        ),
        migrations.AlterField(
            model_name='send_request_files',
            name='sender_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender_id1', to='userapp.request_recordmodel'),
        ),
    ]
