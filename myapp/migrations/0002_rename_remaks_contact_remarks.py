# Generated by Django 4.2 on 2023-04-06 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='remaks',
            new_name='remarks',
        ),
    ]
