# Generated by Django 3.2.15 on 2022-11-07 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
        ('groups', '0006_alter_post_song'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='song',
        ),
        migrations.AddField(
            model_name='post',
            name='songs',
            field=models.ManyToManyField(blank=True, null=True, to='music.Song'),
        ),
    ]
