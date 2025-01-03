from django import forms
from library.library_models.models import User, Book

from .models import UserInteraction, UserRegistration
from django.contrib.auth.forms import UserCreationForm


class UserInteractionForm(forms.ModelForm):
    class Meta:
        model = UserInteraction
        fields = ['action']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'created_at', 'genre', 'description']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_superuser', 'password']
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']

class LikeForm(forms.Form):
    book_id = forms.IntegerField(widget=forms.HiddenInput())

class SaveBookForm(forms.Form):
    book_id = forms.IntegerField(widget=forms.HiddenInput())

class BookSearchForm(forms.Form):
    title = forms.CharField(max_length=200, required=False, label='Title')
    author = forms.CharField(max_length=100, required=False, label='Author')
    genre = forms.CharField(max_length=50, required=False, label='Genre')

class ChangeUsernameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
