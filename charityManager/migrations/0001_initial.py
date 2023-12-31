# Generated by Django 4.2.5 on 2023-09-06 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NgoMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngo_name', models.CharField(max_length=512)),
                ('ngo_phone', models.CharField(max_length=512)),
                ('ngo_email', models.CharField(max_length=512)),
                ('ngo_city', models.CharField(max_length=512)),
                ('ngo_state', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='UserMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=512)),
                ('user_phone', models.CharField(max_length=512)),
                ('user_email', models.CharField(max_length=512)),
                ('user_password', models.CharField(max_length=512)),
                ('user_wallet', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserPref',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_pref', models.CharField(max_length=512)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charityManager.usermaster')),
            ],
        ),
        migrations.CreateModel(
            name='NgoType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngo_type', models.CharField(max_length=512)),
                ('ngo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charityManager.ngomaster')),
            ],
        ),
    ]
