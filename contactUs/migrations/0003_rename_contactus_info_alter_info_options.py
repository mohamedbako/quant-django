# Generated by Django 4.1.7 on 2023-04-06 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactUs', '0002_alter_contactus_options_contactus_email_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contactUS',
            new_name='Info',
        ),
        migrations.AlterModelOptions(
            name='info',
            options={'verbose_name': 'Info', 'verbose_name_plural': 'Infos'},
        ),
    ]
