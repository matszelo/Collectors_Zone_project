# Generated by Django 5.0 on 2024-04-03 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='temat',
            old_name='user',
            new_name='Autor',
        ),
    ]