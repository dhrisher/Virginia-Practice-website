from django.db import models
from django.urls import reverse
# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length = 20)
    nationality = models.CharField(max_length = 20)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('first_app:detail',kwargs={'pk':self.pk})


class Artwork(models.Model):
    name = models.CharField(max_length = 20)
    owner = models.ForeignKey(Owner,related_name = 'art',on_delete=models.CASCADE)
    medium = models.CharField(max_length =20)
    year_painted = models.PositiveIntegerField()

    def __str__(self):
        return self.name
