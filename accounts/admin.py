from django.contrib import admin
from .models import  Profile, Country, Address

# Register your models here.
admin.site.register(Profile)
admin.site.register(Country)
admin.site.register(Address)
