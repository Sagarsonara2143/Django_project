# Generated by Django 4.2 on 2023-04-12 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='', upload_to='profile_pic/'),
            preserve_default=False,
        ),
    ]