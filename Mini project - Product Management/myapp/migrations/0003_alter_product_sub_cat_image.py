# Generated by Django 4.2 on 2023-05-18 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_product_master_alter_product_sub_cat_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_sub_cat',
            name='image',
            field=models.ImageField(default='', upload_to='product_image'),
        ),
    ]