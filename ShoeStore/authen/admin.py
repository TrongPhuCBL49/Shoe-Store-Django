from django.contrib import admin
from .models import CustomerUser
# Register your models here.


class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ['username']


admin.site.register(CustomerUser, CustomerUserAdmin)
