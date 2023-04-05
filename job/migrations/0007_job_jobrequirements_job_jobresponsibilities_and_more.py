# Generated by Django 4.1.7 on 2023-04-05 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_job_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='JobRequirements',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='JobResponsibilities',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='OtherBenifits',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]