# Generated by Django 4.2.2 on 2023-06-12 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='usertype',
            field=models.CharField(choices=[('Artist', 'Artist'), ('Customer', 'Customer')], default='Customer', max_length=100),
        ),
    ]