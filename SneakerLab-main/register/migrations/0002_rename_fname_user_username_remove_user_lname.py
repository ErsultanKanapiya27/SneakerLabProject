# Generated by Django 4.0.2 on 2022-04-18 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='fname',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lname',
        ),
    ]
