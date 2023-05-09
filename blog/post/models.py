from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse
from ckeditor.fields import RichTextField

from account.models import Account


class Author(models.Model):
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.account.first_name} {self.account.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to="images/post")
    date = models.DateField(auto_now=True, blank=True)
    content = RichTextField(validators=[MinLengthValidator(100)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True)

    def __str__(self) -> str:
        return f"[{self.title}] by {self.author.account.first_name} {self.author.account.last_name} on {self.date}"

    def get_absolute_url(self):
        return reverse("url-post", args=[self.pk])


class Comment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=True)
    text = models.TextField(max_length=2048)


class Like(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=True)
