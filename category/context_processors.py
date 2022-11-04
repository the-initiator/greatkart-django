from .models import Category
"""
In all category drop down list, to make it executable we will use python function
context_processers. It takes a request as an argument and it will return the dictionary of data as
a context.
"""

def menu_links(request):
    # it will fetch all the categories from the database
    links = Category.objects.all()
    return dict(links= links) #what it will do?
    # it will bring all the categories list & store them itno above links varibale
