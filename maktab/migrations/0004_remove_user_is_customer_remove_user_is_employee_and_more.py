# Generated by Django 5.0.3 on 2024-04-01 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("maktab", "0003_user_is_admin"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_customer",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_employee",
        ),
        migrations.AddField(
            model_name="user",
            name="is_pupil",
            field=models.BooleanField(default=False, verbose_name="Is Pupil"),
        ),
        migrations.AddField(
            model_name="user",
            name="is_teacher",
            field=models.BooleanField(default=False, verbose_name="Is Teacher"),
        ),
    ]
