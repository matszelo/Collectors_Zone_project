# Generated by Django 5.0 on 2024-03-13 13:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Typ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nazwa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Drop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tytuł', models.CharField(max_length=255)),
                ('Strona', models.CharField(max_length=255)),
                ('Cena', models.CharField(max_length=255)),
                ('Data', models.DateField()),
                ('Godzina', models.TimeField()),
                ('Typ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dropy.typ')),
            ],
        ),
    ]
