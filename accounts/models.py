from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.

class Country(models.Model):
    country_abbr = models.CharField(max_length=3, null=True)
    country_code = models.CharField(max_length=5, null=True)
    country_name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.country_code)+'|'+str(self.country_abbr)

class Profile(models.Model):

    PHONECOUNTRIES = (
        ('+237','+237 CMR'),
        ('+234','+234 NGR'),
        ('+33','+33 FRA'),
        ('+49','+49 GER')
    )

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = RichTextField(null=True, blank=True)
    phoneNumber = models.PositiveIntegerField(null= True, blank=True)
    phoneCountry = models.CharField(max_length=5, choices=PHONECOUNTRIES, default='+237')
    company = models.CharField(max_length=200, null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='ProfileImages/')
    facebook_url = models.CharField(max_length=200, null=True, blank=True)
    twitter_url = models.CharField(max_length=200, null=True, blank=True)
    linkedin_url = models.CharField(max_length=200, null=True, blank=True)
    instagram_url = models.CharField(max_length=200, null=True, blank=True)
    whatsapp_url = models.CharField(max_length=200, null=True, blank=True)
    street = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    country = models.OneToOneField(Country, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Address(models.Model):

    street = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    country = models.OneToOneField(Country, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.city) +' | ' + str(self.country.country_name)






