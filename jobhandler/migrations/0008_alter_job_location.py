# Generated by Django 4.2.6 on 2023-10-11 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobhandler', '0007_rename_locatoin_job_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
