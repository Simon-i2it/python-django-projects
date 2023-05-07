from django.db import models

# Create your models here.


class Account(models.Model):
    username = models.CharField(max_length=100, blank=False)
    # email = models.EmailField(blank=False)
    # password = models.CharField(max_length=30, blank=False)

    def __str__(self) -> str:
        return f"{self.username}"
