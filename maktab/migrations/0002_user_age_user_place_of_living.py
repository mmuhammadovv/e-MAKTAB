# Generated by Django 5.0.3 on 2024-04-09 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("maktab", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="age",
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="place_of_living",
            field=models.CharField(default=1, max_length=55),
            preserve_default=False,
        ),
    ]