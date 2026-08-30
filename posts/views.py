from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, View
from . import models, forms


class FeedView(ListView):
    model = models.Post
    template_name = "posts/feed.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = forms.CommentForm()
        return context


class PostListView(ListView):
    template_name = "posts/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return models.Post.objects.filter(user=self.request.user).prefetch_related("comments", "liked_users")


class PostCreateView(CreateView):
    form_class = forms.PostForm
    template_name = "posts/post_create.html"
    success_url = reverse_lazy("posts:post-list")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)


class LikeView(View):
    def post(self, request, post_pk):
        post = models.Post.objects.get(pk=post_pk)

        if request.user in post.liked_users.all():
            post.liked_users.remove(request.user)
        else:
            post.liked_users.add(request.user)

        return render(request, "posts/feed.html#like-section", {"post": post})


class CommentView(View):
    def post(self, request, post_pk):
        form = forms.CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = get_object_or_404(models.Post, pk=post_pk)
            comment.save()

            return render(request, "posts/feed.html#comment-list", {"post": comment.post})
