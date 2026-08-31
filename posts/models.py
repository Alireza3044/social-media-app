from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    title = models.CharField(max_length=50, db_index=True)
    image = models.ImageField(upload_to="posts/%Y/%m/%d/")
    caption = models.TextField(blank=True)
    slug = models.SlugField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    liked_users = models.ManyToManyField(User, related_name="liked_posts")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "title"],
                name="unique_user_title"
            ),
            models.UniqueConstraint(
                fields=["slug"],
                name="unique_slug"
            )
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "post"],
                name="unique_user_post"
            )
        ]

    def __str__(self):
        return f"{self.user.username} on {self.post.title}"
