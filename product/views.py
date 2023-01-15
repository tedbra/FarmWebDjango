from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from jsonFunctions import read_json,choose_language,Merge

#Imports for posting on the blog and rendering material

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from .forms import ProductEditForm,ProductForm
from django.urls import reverse_lazy

# Create your views here.
param = read_json('js-dj-transfer.JSON').get('param')

class ProductView(ListView):
    model = Product
    template_name= 'products/products-simple.html'
    ordering = ['-date_added']

    def get_context_data (self, **kwargs):
        postData = super(ProductView, self).get_context_data(**kwargs)
        parameters = choose_language(param)
        context = Merge(parameters,postData)
        return context