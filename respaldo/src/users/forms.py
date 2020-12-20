from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from posts.models import Profile
#User = get_user_model()
from posts.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'  # ['username','email','password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']