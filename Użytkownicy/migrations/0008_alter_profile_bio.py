# Generated by Django 5.0 on 2024-03-26 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Użytkownicy', '0007_alter_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
