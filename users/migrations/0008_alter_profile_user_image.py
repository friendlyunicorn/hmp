# Generated by Django 4.0.1 on 2022-02-12 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profile_shop_background'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_image',
            field=models.ImageField(blank=True, upload_to='media/', verbose_name='User avatar'),
        ),
    ]