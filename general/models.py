from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    friends = models.ManyToManyField(
        to="self",
        symmetrical=True,
        blank=True,
    )


class Post(models.Model):
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=64)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


# class Comment(models.Model):
#     body = models.TextField()
#     author = models.ForeignKey(
#         to=User,
#         on_delete=models.CASCADE,
#         related_name="comments"
#     )
#     post = models.ForeignKey(
#         to=Post,
#         on_delete=models.CASCADE,
#         related_name="comments"
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
