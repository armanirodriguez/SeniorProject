# Generated by Django 3.2.15 on 2022-11-13 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
