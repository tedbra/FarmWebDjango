from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'abc@farmweb.com'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        #return 0

class EditUserForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    #is_superuser= forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    #last_login= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    username= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    #is_staff= forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    #is_active= forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    #date_joined= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class PasswordResetForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password2= forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

    # def __init__(self, *args, **kwargs):
    #     super(PasswordResetForm, self).__init__(*args, **kwargs)
    #     self.fields['old_password'].widget.attrs['class'] = 'form-control'
    #     self.fields['new_password1'].widget.attrs['class'] = 'form-control'
    #     self.fields['new_password2'].widget.attrs['class'] = 'form-control'
    #     #return 0

class EditProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        #fields = '__all__'
        fields = ('bio','phoneCountry','phoneNumber','company','profile_pic','facebook_url', 'twitter_url','linkedin_url', 'instagram_url', 'whatsapp_url')

        widgets = {
            'bio' : forms.Textarea(attrs={'class':'form-control'}),
            'phoneNumber' : forms.TextInput(attrs={'class':'form-control'}),
            'company': forms.TextInput(attrs={'class':'form-control'}),
            'facebook_url' : forms.TextInput(attrs={'class':'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class':'form-control'}),
            'linkedin_url' : forms.TextInput(attrs={'class':'form-control'}),
            'instagram_url' : forms.TextInput(attrs={'class':'form-control'}),
            'whatsapp_url' : forms.TextInput(attrs={'class':'form-control'}),
            'phoneCountry': forms.Select(choices='PHONECOUNTRIES', attrs={'class':'form-control'})
        }
        
        
class SignInForm(AuthenticationForm):

    #username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    #password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    
    class Meta :
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
       
