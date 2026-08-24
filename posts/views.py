from django.views.generic import ListView
from . import models


class PostListView(ListView):
    model = models.Post
    context_object_name = "posts"
