# Generated by Django 4.0.1 on 2022-02-08 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0021_remove_jobs_comp'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='comp',
            field=models.CharField(default='false', max_length=100),
        ),
    ]
