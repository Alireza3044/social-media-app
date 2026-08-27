from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    template_name = "posts/form_post_snippet.html"

    class Meta:
        model = Post
        fields = ["title", "image", "caption"]
