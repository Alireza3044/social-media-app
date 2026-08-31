from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, View
from . import models, forms


class FeedView(ListView):
    template_name = "posts/feed.html"
    context_object_name = "posts"

    def get_queryset(self):
        return models.Post.objects.prefetch_related("comments", "liked_users")

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


class PostCardView(View):
    def post(self, request, post_pk):
        post = get_object_or_404(models.Post, pk=post_pk)
        form = forms.CommentForm(request.POST, user=request.user, post=post)
        context = {
            "post": post,
            "form": form
        }
        
        # On Comment Request
        if request.headers.get("Post-Comment"):
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.post = post
                comment.save()

                if request.headers.get("Hx-Request"):
                    return render(request, f"posts/feed.html#post-card", context)
                else:
                    return redirect("posts:feed")
            else:
                if request.headers.get("Hx-Request"):
                    return render(request, f"posts/feed.html#post-card", context)
                else:
                    return redirect("posts:feed")
        
        # On Like Request
        elif request.headers.get("Post-Like"):
            post = models.Post.objects.get(pk=post_pk)

            if request.user in post.liked_users.all():
                post.liked_users.remove(request.user)
            else:
                post.liked_users.add(request.user)

            if request.headers.get("Hx-Request"):
                return render(request, f"posts/feed.html#post-card", context)
            else:
                return redirect("posts:feed")

        # On Everything Else
        else:
            return redirect("posts:feed")
