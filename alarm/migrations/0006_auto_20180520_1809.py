# Generated by Django 2.0 on 2018-05-20 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alarm', '0005_alarm_song'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alarm',
            old_name='song',
            new_name='tone',
        ),
    ]
