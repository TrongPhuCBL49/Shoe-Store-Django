from django.contrib import admin
from .models import CustomerUser, GuestEmail    
# Register your models here.


class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ['username']


admin.site.register(CustomerUser, CustomerUserAdmin)

admin.site.register(GuestEmail)
