# Generated by Django 2.0.9 on 2018-10-20 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='insert_blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_post_name', models.TextField()),
                ('image_name', models.TextField()),
                ('user_id', models.IntegerField()),
                ('category', models.TextField(choices=[('Technology', 'tech'), ('sports', 'sports'), ('fasion', 'fasion')])),
                ('Date_of_publish', models.DateField(auto_now=True)),
            ],
        ),
    ]
