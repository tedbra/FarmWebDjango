from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Tag(models.Model):
    name=models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('inStock','inStock'),
        ('outStock', 'outStock')
    )

    QUANTITY_TAG = (
        ('kg','kg'),
        ('bucket','bucket'),
        ('litres','litres'),
        ('bags','bags')
    )

    COUNTRY = (
        ('Cameroon','Cameroon'),
        ('Chad','Chad'),
        ('Nigeria','Nigeria'),
        ('Gabon','Gabon'),
        ('Equatorial Guinea','Equatorial Guinea'),
        ('Central African Republic','Central African Republic'),
        ('Congo Republic','Congo Republic'),
        ('Democratic Republic of Congo','Democratic Republic of Congo'),
        ('Ghana','Ghana'),
        ('Togo','Togo'),
        ('Senegal','Senegal'),
        ('Guinea','Guinea')
    )

    name=models.CharField(max_length=200, null=True)
    price=models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = RichTextField(null=True, blank=True)
    date_added=models.DateTimeField(auto_now_add=True, null=True)
    quantity = models.FloatField(null=True)
    quantity_tag = models.CharField(max_length=20, default='kg',choices=QUANTITY_TAG)
    tags = models.CharField(max_length=200, null=True, blank=True)
    product_picture = models.ImageField(null=True, blank=True, upload_to='ProductImages/')
    street = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=50,choices=COUNTRY, default='Cameroon')

    def __str__(self):
        return self.name







