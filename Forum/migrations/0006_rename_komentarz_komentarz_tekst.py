# Generated by Django 5.0 on 2024-04-14 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0005_alter_komentarz_temat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='komentarz',
            old_name='Komentarz',
            new_name='Tekst',
        ),
    ]
