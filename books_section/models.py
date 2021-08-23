from django.db import models

# Create your models here.

class BookModel(models.Model):
    isbn = models.CharField(max_length=50, null=False, blank=True)
    title = models.CharField(max_length=300, null=True, blank=True)
    author = models.CharField(max_length=300, null=True, blank=True)
    year_of_publication = models.CharField(max_length=300, null=True, blank=True)
    publisher = models.CharField(max_length=300, null=True, blank=True)
    image_url_s = models.CharField(null=True, blank=True ,max_length=300)
    image_url_m = models.CharField(null=True, blank=True ,max_length=300)
    image_url_l = models.CharField(null=True, blank=True ,max_length=300)

    def __str__(self):
        return f'{self.title}'