# Generated by Django 2.0.9 on 2018-10-20 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20181020_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='blog_url',
            field=models.TextField(),
        ),
    ]