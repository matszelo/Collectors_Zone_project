# Generated by Django 5.0 on 2023-12-27 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_site', '0003_alter_kategoria_nazwa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kategoria',
            name='Nazwa',
            field=models.CharField(max_length=50),
        ),
    ]