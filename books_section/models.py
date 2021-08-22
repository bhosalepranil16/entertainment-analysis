from django.db import models

# Create your models here.

class BookModel(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year_of_publication = models.IntegerField()
    publisher = models.CharField(max_length=200)
    image_url = models.URLField()