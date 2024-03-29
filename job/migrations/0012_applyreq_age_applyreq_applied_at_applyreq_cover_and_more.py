# Generated by Django 4.1.7 on 2023-04-06 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_remove_applyreq_age_remove_applyreq_applied_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyreq',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='applyreq',
            name='applied_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='applyreq',
            name='cover',
            field=models.CharField(default='', max_length=350),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applyreq',
            name='cv',
            field=models.FileField(default='', upload_to='apply/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applyreq',
            name='email',
            field=models.EmailField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applyreq',
            name='linkedIn',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applyreq',
            name='location',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applyreq',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
