# from django import forms

# from .models import Product


# class ProductForm(forms.ModelForm):

#     class Meta:
#         model = Product 
#         fields = ('name','price','category','description')

#         widgets = {
#             'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Product Name'}),
#             'price': forms.TextInput(attrs={'class':'form-control','placeholder':'Price of Product'}),
#             'category' : forms.Select(choices='CATEGORY', attrs={'class':'form-control','placeholder':'Select the category'}),
#             'description' : forms.Textarea(attrs={'class':'form-control','placeholder':'Type your article here'}),
#             #'tag' : forms.Select(attrs={'class':'form-control','placeholder':'Select the Author'}),
#         }
  

# class ProductEditForm(forms.ModelForm):
#     class Meta:
#      model = Product 
#      fields = '__all__'

#      widgets = {
#         'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Product Name'}),
#         'price': forms.TextInput(attrs={'class':'form-control','placeholder':'Price of Product'}),
#         'category' : forms.Select(choices='CATEGORY', attrs={'class':'form-control','placeholder':'Select the category'}),
#         'description' : forms.Textarea(attrs={'class':'form-control','placeholder':'Product description'}),
#         #'tag' : forms.Select(attrs={'class':'form-control','placeholder':'Select the Author'}),
#      }





