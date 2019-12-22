from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
# Create your models here.


class CustomerUserManager(UserManager):
    def create_superuser(self, username, email, first_name, last_name, phone_number, country, province, district, address, postcode, password=None):
        user_obj = self.model(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_staff=True,
            is_active=True,
            is_superuser=True,
            phone_number=phone_number,
            country=country,
            province=province,
            district=district,
            address=address,
            postcode=postcode,

        )
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj


class CustomerUser(AbstractUser):
    phone_number = models.CharField(max_length=15, default='')
    country = models.CharField(max_length=50, default='')
    province = models.CharField(max_length=50, default='')
    district = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=255, default='')
    postcode = models.CharField(max_length=10, default='')

    objects = CustomerUserManager()

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
