# Generated by Django 4.1.7 on 2023-04-05 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_applyreq_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyreq',
            name='applied_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
