# Generated by Django 4.1.2 on 2022-11-03 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='confidentialdatamodel',
            name='published_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='confidentialdatamodel',
            name='status',
            field=models.CharField(default='pending', max_length=20),
        ),
    ]
