# Generated by Django 5.0.3 on 2024-04-01 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("maktab", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_admin",
        ),
    ]