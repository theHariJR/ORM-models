# Generated by Django 5.1 on 2024-09-21 12:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('capno', models.IntegerField(primary_key=True, serialize=False)),
                ('coname', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Capital',
            fields=[
                ('capname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('capno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.country')),
            ],
        ),
    ]