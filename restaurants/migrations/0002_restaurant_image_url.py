# Generated by Django 5.0.1 on 2024-07-18 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurants", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="restaurant",
            name="image_url",
            field=models.URLField(blank=True, null=True),
        ),
    ]
