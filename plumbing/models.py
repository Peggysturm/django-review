from django.db import models
from django.urls import reverse

class Plumbing(models.Model):
    name = models.CharField(max_length=300, verbose_name="Имя товара")
    slug = models.SlugField(max_length=300)
    link = models.URLField(max_length=300)
    price = models.CharField(max_length=50)


    def str(self):
        return self.name


    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug':self.slug})


class PlumbingDetails(models.Model):
    plumbing = models.OneToOneField(Plumbing, on_delete=models.CASCADE, verbose_name="Детели", related_name="details",null=True)
    description = models.TextField()
    raiting = models.IntegerField(null=True)