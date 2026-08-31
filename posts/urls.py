from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.PostListView.as_view(), name="post-list"),
    path("create/", views.PostCreateView.as_view(), name="post-create"),
    path("feed/", views.FeedView.as_view(), name="feed"),
    path("post-card/<int:post_pk>/", views.PostCardView.as_view(), name="post-card"),
]
