# Generated by Django 4.1 on 2022-12-30 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_address_city'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Address',
        ),
    ]
