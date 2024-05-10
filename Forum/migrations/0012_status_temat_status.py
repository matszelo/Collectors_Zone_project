# Generated by Django 5.0 on 2024-05-10 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0011_remove_temat_status_delete_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nazwa', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='temat',
            name='Status',
            field=models.CharField(default='Otwarty'),
        ),
    ]
