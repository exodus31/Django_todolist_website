# Generated by Django 4.0.1 on 2022-02-07 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0018_alter_jobs_x'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='x',
        ),
    ]
