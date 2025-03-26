from django import forms
from . models import Post, Comment
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from taggit.forms import TagField

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email")

class PostForm(forms.ModelForm):
    tags = TagField()
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]

class CommentForm(forms.ModelForm):
    tags = TagField()
    class Meta:
        model = Comment
        fields = ['content']

