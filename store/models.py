from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    product_name   = models.CharField(max_length = 200, unique = True)
    slug           = models.SlugField(max_length = 200, unique = True)
    description    = models.TextField(max_length = 200, blank = True)
    price          = models.IntegerField()
    images         = models.ImageField(upload_to = 'photos/products')
    stock          = models.IntegerField(default = True)
    is_available   = models.BooleanField(default =True)
    """ this category is the foreign key. first specify the category and see what
    should happen to the product when we delete the category. Here we use "models.CASCASE"
    whenever we delete the products attached to that category will be deleted"""
    category       = models.ForeignKey(Category, on_delete = models.CASCADE)
    created_date   = models.DateTimeField(auto_now_add = True)
    modified_date  = models.DateTimeField(auto_now = True)


    def get_url(self):
        # product_detail is the name of the url
        return reverse('product_detail', args = [self.category.slug, self.slug])
#self.category means class Product->category and "self.category.slug" means category folder->models.py slug
# things are interconnected but bxz of ForeignKey we can use
#self.slug means self is class Product -> slug
    def __str__(self):
        return self.product_name
