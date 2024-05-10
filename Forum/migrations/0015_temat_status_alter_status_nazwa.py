# Generated by Django 5.0 on 2024-05-10 08:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0014_alter_status_nazwa'),
    ]

    operations = [
        migrations.AddField(
            model_name='temat',
            name='Status',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Forum.status'),
        ),
        migrations.AlterField(
            model_name='status',
            name='Nazwa',
            field=models.CharField(max_length=10),
        ),
    ]