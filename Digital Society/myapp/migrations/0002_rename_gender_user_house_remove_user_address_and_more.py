# Generated by Django 4.2.1 on 2023-05-29 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='gender',
            new_name='house',
        ),
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.AddField(
            model_name='user',
            name='usertype',
            field=models.CharField(default='member', max_length=50),
        ),
    ]
