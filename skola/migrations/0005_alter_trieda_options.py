# Generated by Django 5.1.1 on 2024-12-11 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skola', '0004_trieda'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trieda',
            options={'ordering': ['nazov'], 'verbose_name': 'Trieda', 'verbose_name_plural': 'Triedy'},
        ),
    ]
