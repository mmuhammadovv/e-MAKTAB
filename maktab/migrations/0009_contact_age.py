# Generated by Django 5.0.4 on 2024-04-26 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("maktab", "0008_delete_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="age",
            field=models.IntegerField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
