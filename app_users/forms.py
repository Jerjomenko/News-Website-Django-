from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile, News, Coments

# Моё мнение в самой регистрации не должно быть лишних полей.
class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class AuthForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileForm(ModelForm):

    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=20, required=False)
    email = forms.EmailField(required=False)

    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "email",  "city", "tel"]



class NewsForm(ModelForm):

    class Meta:
        model = News
        fields = ["title", "text", "my_image"]



class ComentForm(ModelForm):

    class Meta:
        model = Coments
        fields = ["text"]

