# Generated by Django 4.2.1 on 2023-05-29 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_gender_user_house_remove_user_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='house',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='usertype',
            field=models.CharField(default='member', max_length=100),
        ),
    ]
