# Generated by Django 4.1.7 on 2023-04-06 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_applyreq_applied_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applyreq',
            name='age',
        ),
        migrations.RemoveField(
            model_name='applyreq',
            name='applied_at',
        ),
        migrations.RemoveField(
            model_name='applyreq',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='applyreq',
            name='cv',
        ),
        migrations.RemoveField(
            model_name='applyreq',
            name='email',
        ),
        migrations.RemoveField(
            model_name='applyreq',
            name='linkedIn',
        ),
        migrations.RemoveField(
            model_name='applyreq',
            name='location',
        ),
        migrations.RemoveField(
            model_name='applyreq',
            name='phone',
        ),
    ]