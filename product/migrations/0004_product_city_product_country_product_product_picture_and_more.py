# Generated by Django 4.1 on 2023-01-07 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_product_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='city',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='country',
            field=models.CharField(choices=[('Cameroon', 'Cameroon'), ('Chad', 'Chad'), ('Nigeria', 'Nigeria'), ('Gabon', 'Chad'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Central African Republic', 'Central African Republic'), ('Congo Republic', 'Congo Republic'), ('Democratic Republic of Congo', 'Democratic Republic of Congo'), ('Ghana', 'Ghana'), ('Togo', 'Togo'), ('Senegal', 'Senegal'), ('Guinea', 'Guinea')], default='Cameroon', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='product_picture',
            field=models.ImageField(blank=True, null=True, upload_to='ProductImages/'),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity_tag',
            field=models.CharField(choices=[('kg', 'kg'), ('bucket', 'bucket'), ('litres', 'litres'), ('bags', 'bags')], default='kg', max_length=20),
        ),
        migrations.AddField(
            model_name='product',
            name='street',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='product.tag'),
        ),
    ]
