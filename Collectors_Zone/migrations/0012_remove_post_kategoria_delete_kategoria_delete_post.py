# Generated by Django 5.0 on 2024-03-13 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Collectors_Zone', '0011_typ_drop_typ'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Kategoria',
        ),
        migrations.DeleteModel(
            name='Kategoria',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
