# Generated by Django 3.2.12 on 2022-03-25 17:49
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('adserver_auth', '0004_adding_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaluser',
            name='notify_on_completed_flights',
            field=models.BooleanField(default=True, help_text='Receive an email notification when an advertising flight is complete'),
        ),
        migrations.AddField(
            model_name='user',
            name='notify_on_completed_flights',
            field=models.BooleanField(default=True, help_text='Receive an email notification when an advertising flight is complete'),
        ),
    ]
