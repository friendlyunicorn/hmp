# Generated by Django 4.0.1 on 2022-02-12 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='IMG_20220129_201111_236-01-01.jpeg', upload_to='', verbose_name='Image'),
        ),
    ]
