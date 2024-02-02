# Generated by Django 3.2.20 on 2024-01-25 00:37
import pgvector.django
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adserver_analyzer', '0003_add_embeddings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analyzedurl',
            name='embedding',
            field=pgvector.django.VectorField(blank=True, default=None, dimensions=384, null=True),
        ),
        migrations.AlterField(
            model_name='historicalanalyzedurl',
            name='embedding',
            field=pgvector.django.VectorField(blank=True, default=None, dimensions=384, null=True),
        ),
    ]
