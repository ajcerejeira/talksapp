# Generated by Django 3.2.3 on 2021-05-20 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("talks", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="talk",
            name="tags",
            field=models.JSONField(default=list),
        ),
    ]