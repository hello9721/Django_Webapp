# Generated by Django 4.1.3 on 2022-11-30 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Pro_02", "0002_rename_blog_me"),
    ]

    operations = [
        migrations.RenameField(
            model_name="me",
            old_name="main",
            new_name="url",
        ),
        migrations.AddField(
            model_name="me",
            name="singer",
            field=models.CharField(default="", max_length=20),
        ),
    ]
