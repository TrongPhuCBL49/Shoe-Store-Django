from django.db import models

from billing.models import BillingProfile

# ADDRESS_TYPES = (
#     ('billing', 'Billing'),
#     ('shipping', 'Shipping'),
# )

class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, on_delete=models.DO_NOTHING)
    # address_type    = models.CharField(max_length=120, choices=ADDRESS_TYPES)
    address         = models.CharField(max_length=120)
    district        = models.CharField(max_length=120)
    province        = models.CharField(max_length=120)
    country         = models.CharField(max_length=120, default='Viet Nam')
    postcode        = models.CharField(max_length=120)

    def __str__(self):
        return str(self.billing_profile)