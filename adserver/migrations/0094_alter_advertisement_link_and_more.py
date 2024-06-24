# Generated by Django 4.2.11 on 2024-05-23 23:46
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("adserver", "0093_publisher_ignore_mobile_traffic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="advertisement",
            name="link",
            field=models.URLField(
                help_text="URL of your landing page. This may contain UTM parameters so you know the traffic came from us. The publisher will be added in the 'ea-publisher' query parameter.",
                max_length=1024,
                verbose_name="Link URL",
            ),
        ),
        migrations.AlterField(
            model_name="historicaladvertisement",
            name="link",
            field=models.URLField(
                help_text="URL of your landing page. This may contain UTM parameters so you know the traffic came from us. The publisher will be added in the 'ea-publisher' query parameter.",
                max_length=1024,
                verbose_name="Link URL",
            ),
        ),
    ]