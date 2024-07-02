from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from .models import User, Post

class UserCreationForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content', 'image')
