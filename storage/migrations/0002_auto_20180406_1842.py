# Generated by Django 2.0 on 2018-04-06 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filesong',
            name='height',
        ),
        migrations.RemoveField(
            model_name='filesong',
            name='width',
        ),
        migrations.RemoveField(
            model_name='filevideo',
            name='album',
        ),
        migrations.RemoveField(
            model_name='filevideo',
            name='artist',
        ),
        migrations.AddField(
            model_name='filesong',
            name='album',
            field=models.CharField(blank=True, max_length=42),
        ),
        migrations.AddField(
            model_name='filesong',
            name='artist',
            field=models.CharField(blank=True, max_length=42),
        ),
        migrations.AddField(
            model_name='filevideo',
            name='height',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='filevideo',
            name='width',
            field=models.PositiveIntegerField(default=0),
        ),
    ]