from django.urls import path
from .views import UserRegisterView,UserSignInView, EditProfileView, MyProfileView
from .views import UserProfileView,UserEditView, PasswordResetView, PasswordResetSuccessView, CreateProfileView
#from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('signin/', UserSignInView.as_view(), name='signin'),
    path('edit-User/', UserEditView.as_view(), name='edit-User'),
    path('my-profile/', MyProfileView.as_view(), name='my-profile'),
    #path('password/',auth_views.PasswordChangeView.as_view(template_name='registration/password-reset.html'), name='password-reset'),
    path('password/',PasswordResetView.as_view(), name='password-reset'),
    path('password-changed/',PasswordResetSuccessView, name='password-success'),
    path('<int:pk>/profile/',UserProfileView.as_view(), name='user-profile'),
    path('<int:pk>/edit_profile/',EditProfileView.as_view(), name='edit-profile'),
    path('create_profile/',CreateProfileView.as_view(), name='create-profile'),
]