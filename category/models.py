# https://docs.djangoproject.com/en/4.1/topics/db/models/
# A model is the single, definitive source of information about your data.
# It contains the essential fields and behaviors of the data you’re storing.
# Generally, each model maps to a single database table.
from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length = 50, unique = True)
    slug = models.SlugField(max_length = 100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)


    """
    django makes the model name into plural by adding "s" e.g categorys which is not good.
    to solve this issue use class Meta
    """

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
# belwo func bring the url of particular category in navbar.html
    def get_url(self):# self bcz func inside the model
        return reverse('products_by_category', args =[self.slug]) # self.slug means class Category slug

    def __str__(self):
        return self.category_name
