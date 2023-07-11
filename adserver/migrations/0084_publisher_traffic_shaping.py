# Generated by Django 3.2.18 on 2023-07-07 23:19
import jsonfield.fields
from django.db import migrations

import adserver.validators


class Migration(migrations.Migration):

    dependencies = [
        ('adserver', '0083_allow_api_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='traffic_cap',
            field=jsonfield.fields.JSONField(blank=True, default=None, null=True, validators=[adserver.validators.TrafficFillValidator()], verbose_name='Traffic cap'),
        ),
        migrations.AddField(
            model_name='flight',
            name='traffic_fill',
            field=jsonfield.fields.JSONField(blank=True, default=None, null=True, validators=[adserver.validators.TrafficFillValidator()], verbose_name='Traffic fill'),
        ),
        migrations.AddField(
            model_name='historicalflight',
            name='traffic_cap',
            field=jsonfield.fields.JSONField(blank=True, default=None, null=True, validators=[adserver.validators.TrafficFillValidator()], verbose_name='Traffic cap'),
        ),
        migrations.AddField(
            model_name='historicalflight',
            name='traffic_fill',
            field=jsonfield.fields.JSONField(blank=True, default=None, null=True, validators=[adserver.validators.TrafficFillValidator()], verbose_name='Traffic fill'),
        ),
    ]
