# Generated by Django 4.2.5 on 2023-09-06 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charityManager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ngotype',
            old_name='ngo_id',
            new_name='ngo',
        ),
        migrations.RenameField(
            model_name='userpref',
            old_name='user_id',
            new_name='user',
        ),
    ]