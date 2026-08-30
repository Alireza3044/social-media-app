from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    template_name = "accounts/form_snippet.html"

    class Meta:
        model = Post
        fields = ["title", "image", "caption"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
