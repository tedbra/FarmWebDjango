# Generated by Django 4.1 on 2023-01-03 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_remove_comment_posts_alter_comment_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]