# Generated by Django 3.1.3 on 2020-11-25 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0008_auto_20201125_0136"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="avatar",
            new_name="discord_avatar",
        ),
    ]
