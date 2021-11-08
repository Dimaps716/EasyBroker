# Generated by Django 3.1.4 on 2021-11-08 01:32

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent', models.CharField(blank=True, max_length=80, null=True)),
                ('public_id', models.CharField(blank=True, max_length=20, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('title_image_url', models.URLField(blank=True, null=True)),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('parking_spaces', models.IntegerField()),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('property_type', models.CharField(blank=True, max_length=100, null=True)),
                ('operations', django.contrib.postgres.fields.jsonb.JSONField()),
                ('updated_at', models.DateField()),
                ('show_prices', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.IntegerField(default=1)),
                ('limit', models.IntegerField(default=20)),
                ('status_request', models.CharField(choices=[('INITIATED', 'INITIATED'), ('EXTRACT_DATA', 'EXTRACT_DATA'), ('WRITING_REPORT', 'WRITING_REPORT'), ('FINALIZED', 'FINALIZED'), ('ERROR', 'ERROR')], default='INITIATED', max_length=15)),
                ('error_message', models.CharField(blank=True, max_length=200, null=True)),
                ('report', models.FileField(blank=True, null=True, upload_to='requests')),
            ],
        ),
    ]
