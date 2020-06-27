from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from core.models import CoreModel as CM


class ClientProfile(CM):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='client_profile')



class RestaurantProfile(CM):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='restaurant_profile')
#    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='vendor_address')

