from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.PostListView.as_view(), name="post-list"),
    path("create/", views.PostCreateView.as_view(), name="post-create"),
    path("feed/", views.FeedView.as_view(), name="feed"),
    path("like/<int:post_pk>/", views.LikeView.as_view(), name="like"),
]
