# Generated by Django 5.0 on 2024-04-14 10:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0002_rename_user_temat_autor'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='temat',
            name='Autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Komentarz', models.TextField()),
                ('Dodano', models.DateTimeField(auto_now_add=True)),
                ('Autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Temat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Forum.temat')),
            ],
        ),
    ]
