from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, null=True)
    genre = models.CharField(max_length=200, null=True)
    published_date = models.DateField(null=True)
    isbn = models.CharField(max_length=200, null=True)
