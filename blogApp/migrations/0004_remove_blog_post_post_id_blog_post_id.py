# Generated by Django 4.2.3 on 2023-08-27 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0003_remove_blog_post_id_alter_blog_post_post_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog_post',
            name='post_id',
        ),
        migrations.AddField(
            model_name='blog_post',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
