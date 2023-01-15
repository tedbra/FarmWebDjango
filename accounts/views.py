from django.shortcuts import render, get_object_or_404
from jsonFunctions import read_json,choose_language, Merge
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView, LoginView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditUserForm, PasswordResetForm, EditProfileForm, SignInForm
from .models import Profile
#from app.models import model #from that app
# Create your views here.

param = read_json('js-dj-transfer.JSON').get('param')

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('create-profile')

    def get_context_data (self, **kwargs):
        postData = super(UserRegisterView, self).get_context_data(**kwargs)
        parameters = choose_language(param)
        context = Merge(parameters,postData)
        return context

class UserSignInView(LoginView):
    form_class = SignInForm
    template_name = 'registration/signIn.html'
    success_url = reverse_lazy('home')

    def get_context_data (self, **kwargs):
        postData = super(UserSignInView, self).get_context_data(**kwargs)
        parameters = choose_language(param)
        context = Merge(parameters,postData)
        return context

class UserEditView(generic.UpdateView):
    form_class = EditUserForm
    template_name = 'registration/edit_User.html'
    success_url = reverse_lazy('my-profile')

    def get_object(self):
        return self.request.user

    def get_context_data(self, *args, **kwargs):
        postData = super(UserEditView, self).get_context_data(*args,**kwargs)
        parameters = choose_language(param)
        context = Merge(parameters,postData)
        return context

class PasswordResetView(PasswordChangeView):
    form_class = PasswordResetForm
    success_url = reverse_lazy('password-success')
    template_name='registration/password-reset.html'

    def get_context_data(self, **kwargs):
        postData = super(PasswordResetView, self).get_context_data(**kwargs)
        parameters = choose_language(param)
        context = Merge(parameters,postData)
        return context

def PasswordResetSuccessView(request):
    context = choose_language(param)
    return render(request, 'registration/password_success.html', context)

class MyProfileView(generic.DetailView):    
    form_class = EditUserForm
    template_name = 'registration/my_profile.html'

    def get_object(self):
        return self.request.user

    def get_context_data(self, *args, **kwargs):
        postData = super(MyProfileView, self).get_context_data(*args,**kwargs)
        parameters = choose_language(param)
        context = Merge(parameters,postData)
        return context


class UserProfileView(generic.DetailView):    
    model = Profile
    #form_class = EditProfileForm
    template_name = 'registration/profile.html'

    def get_object(self):
        return self.request.user

    def get_context_data(self, *args, **kwargs):
        #users = Profile.objects.all() #This function helps to grab all the users data but not necessary here as we only need to grab a specific user
        postData = super(UserProfileView, self).get_context_data(*args,**kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk']) # this permits to send out the data of the Profile for that id
        parameters = choose_language(param)
        context = Merge(parameters,postData)
        context['page_user'] = page_user
        return context

class EditProfileView(generic.UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    #fields = ['bio', 'profile_pic', 'whatsapp_url', 'facebook_url', 'twitter_url', 'linkedin_url','instagram_url']
    success_url = reverse_lazy('my-profile')

    def get_context_data(self, *args, **kwargs):
        parameters = choose_language(param)
        postData = super(EditProfileView, self).get_context_data(*args,**kwargs)
        context = Merge(parameters,postData)
        return context


class CreateProfileView(generic.CreateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'registration/create_profile.html'
    success_url = reverse_lazy('my-profile')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        parameters = choose_language(param)
        postData = super(CreateProfileView, self).get_context_data(*args,**kwargs)
        context = Merge(parameters,postData)
        return context






