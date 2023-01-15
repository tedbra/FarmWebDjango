#from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post, Category , Comment


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1', 'password2']


#cats = [('coding','coding'),('sports','sports'),('love','love')] #hard coded which is also possible
cats = Category.objects.all().values_list('name','name')
cats_list = []
for item in cats:
    cats_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
     model = Post
     fields = ('title','author','category','body','post_picture')

     widgets = {
        'title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Title'}),
        'author' : forms.Select(attrs={'class':'form-control','placeholder':'Select the Author'}),
        'category' : forms.Select(choices=cats_list, attrs={'class':'form-control','placeholder':'Select the category'}),
        'body' : forms.Textarea(attrs={'class':'form-control','placeholder':'Type your article here'}),
     }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Category'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'my_comment')

        widgets = {
            'my_comment':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter your comment'}),
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
        }                      



