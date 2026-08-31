from django import forms
from django.core.exceptions import ValidationError
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

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        self.post = kwargs.pop("post", None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()

        if self.user and self.post and Comment.objects.filter(user=self.user, post=self.post).exists():
            raise ValidationError("You have already commented on this post.",code='duplicate_comment')

        return cleaned_data
