# Generated by Django 4.1.1 on 2022-10-12 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("groups", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="community",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
