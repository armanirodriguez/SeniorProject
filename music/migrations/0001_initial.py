# Generated by Django 4.1.1 on 2022-10-24 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Song",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("song_id", models.CharField(max_length=100)),
                ("song_name", models.CharField(max_length=50)),
            ],
        ),
    ]
