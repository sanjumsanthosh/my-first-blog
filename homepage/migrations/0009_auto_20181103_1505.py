# Generated by Django 2.0.9 on 2018-11-03 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_auto_20181103_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insert_blog',
            name='view_counter',
            field=models.IntegerField(default=0),
        ),
    ]