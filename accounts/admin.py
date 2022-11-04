from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.



"""   for custom passowd """
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login','date_joined','is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login','date_joined')
    ordering = ('-date_joined',)


    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()



""" now delete the by default db.sqllite3 becasue now we have custom login &
in category folder -> migrations -> 0001_initial.py & 0002 delete them as well"""
admin.site.register(Account, AccountAdmin)
