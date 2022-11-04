from django.contrib import admin
from .models import Category
# Register your models here. https://docs.djangoproject.com/en/4.1/ref/contrib/admin/
"""https://docs.djangoproject.com/en/4.1/topics/migrations/
now run commands: python3 manage.py makemigrations because makemigrations is responsible
for packaging up your model changes into individual migration files - analogous to
commits - and migrate is responsible for applying those to your database.
"""


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
admin.site.register(Category,CategoryAdmin)
