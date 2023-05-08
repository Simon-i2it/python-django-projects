from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse

from account.models import Account


class Author(models.Model):
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.account.first_name} {self.account.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=500)
    image = models.CharField(max_length=254)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(100)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return f"[{self.title}] by {self.author.account.first_name} {self.author.account.last_name} on {self.date}"

    def get_absolute_url(self):
        return reverse("url-post", args=[self.slug])


class Comment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=True)
    text = models.TextField(max_length=2048)


class Like(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=True)
