# Generated by Django 2.1.5 on 2019-02-11 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190208_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='desc',
            field=models.TextField(default='A simple description will suffice', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='Cowboy Bebop: Ultimate Anime Analysis', max_length=200),
        ),
    ]