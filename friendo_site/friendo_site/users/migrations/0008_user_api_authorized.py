# Generated by Django 3.1.3 on 2020-12-03 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_delete_authtoken"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="api_authorized",
            field=models.BooleanField(default=False),
        ),
    ]
