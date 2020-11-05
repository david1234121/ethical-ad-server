# Generated by Django 2.2.13 on 2020-10-28 19:39
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('adserver', '0036_update_docstrings'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='render_pixel',
            field=models.BooleanField(default=True, help_text='Render ethical-pixel in ad templates. This is needed for users not using the ad client.'),
        ),
    ]