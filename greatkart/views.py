from django.shortcuts import render
from store.models import Product
def home(request):
    """ objects.all uses bcz now all products are avalbe but you can change to product is_not_available"""
    products = Product.objects.all().filter(is_available = True)

    context = {
        'products': products,
    }

    """ now this file will be avialbe in home.html site"""
    return render(request, 'home.html',context)
