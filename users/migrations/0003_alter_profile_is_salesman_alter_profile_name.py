# Generated by Django 4.0.1 on 2022-02-11 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_is_salesman_alter_profile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='is_salesman',
            field=models.BooleanField(default=False, verbose_name='Is Salesman'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
    ]