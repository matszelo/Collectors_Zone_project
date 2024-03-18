# Generated by Django 5.0 on 2024-03-13 12:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nazwa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tytuł', models.CharField(max_length=255)),
                ('Opis', models.TextField()),
                ('Kategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Posty.kategoria')),
            ],
        ),
    ]
