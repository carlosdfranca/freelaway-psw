# Generated by Django 4.0.3 on 2022-04-08 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_jobs_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='arquivo_final',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
