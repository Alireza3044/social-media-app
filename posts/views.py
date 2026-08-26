from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from . import models, forms


class FeedView(ListView):
    model = models.Post
    template_name = "posts/post_list.html"
    context_object_name = "posts"


class PostListView(ListView):
    template_name = "posts/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return models.Post.objects.filter(user=self.request.user)


class PostCreateView(CreateView):
    form_class = forms.PostForm
    template_name = "posts/post_create.html"
    success_url = reverse_lazy("posts:post-list")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)
