# Generated by Django 5.1.7 on 2025-03-31 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_categoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='descrição',
            new_name='descricao',
        ),
    ]
