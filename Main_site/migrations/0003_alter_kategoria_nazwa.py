# Generated by Django 5.0 on 2023-12-27 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_site', '0002_kategoria_alter_post_kategoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kategoria',
            name='Nazwa',
            field=models.CharField(max_length=20),
        ),
    ]