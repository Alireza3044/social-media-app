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
        widgets = {
            "body": forms.Textarea({
                "class": "w-full h-24 bg-gray-100 border-2 border-gray-400 rounded-lg px-2 py-1 resize-none",
                "placeholder": "Write a comment..."
            })
        }
        labels = {
            "body": ""
        }
