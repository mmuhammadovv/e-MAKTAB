# Generated by Django 5.0.3 on 2024-04-01 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("maktab", "0002_remove_user_is_admin"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_admin",
            field=models.BooleanField(default=False, verbose_name="Is admin"),
        ),
    ]