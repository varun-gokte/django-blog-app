# Generated by Django 4.2.3 on 2023-08-27 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_blog_post_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog_post',
            name='id',
        ),
        migrations.AlterField(
            model_name='blog_post',
            name='post_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]