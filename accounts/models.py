from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
""" Django by default you must use username as login field. So what we will do? Instead of using django default authorization
system we will create our custom user model. In order to do so first create app.
run command: python3 manage.py startapp accounts """
# creae a login system for  normal user
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('user must have an email address')

        if not username:
            raise ValueError('user must have an useranme')


        user = self.model(
# if someone enter emial in capital then just normalize and use as small letters
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )


        # inbuilt function to set the passwrod
        user.set_password(password)
        user.save(using = self._db)
        return user

# creae a login system for  superuser
    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )

        # superuser will has all permissions
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using = self._db)
        return user


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    username   = models.CharField(max_length=50,unique = True)
    email      = models.EmailField(max_length=100, unique = True)
    phone_number = models.CharField(max_length=50)
    # requied filters manadotry while creating custom user system
    date_joined = models.DateTimeField(auto_now_add = True)
    last_login = models.DateTimeField(auto_now_add = True)
    is_admin = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = False)
    is_superadmin = models.BooleanField(default = False)


    # we want to use emial in place of username

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name','last_name']

    objects = MyAccountManager()


    """we are returning the account object inside the template,
     so this should return emial address"""
    def __str__(self):
        return self.email


    """ if the user is admin then he has all the permissions """
    def has_perm(self,perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
