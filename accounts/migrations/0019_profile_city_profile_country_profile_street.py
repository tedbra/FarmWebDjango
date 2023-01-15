# Generated by Django 4.1 on 2023-01-08 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_delete_product_delete_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.country'),
        ),
        migrations.AddField(
            model_name='profile',
            name='street',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
