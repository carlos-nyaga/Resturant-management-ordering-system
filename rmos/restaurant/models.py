from django.db import models
from django.utils.translation import ugettext_lazy as _
#from django.urls import reverse

from core.models import CoreModel as CM
from account.models import ClientProfile, RestaurantProfile

class Menu(CM):
    """
    Restaurant Menu Item
    """

    SOUP = "Soup"
    SALAD = "Salad"
    MAIN_DISH = "Main Dish"                 # 1000g = 1Kg
    DESSERT = "Dessert"     # 1000ml = 1L
    BEVERAGE = "Beverage"


    ITEM_CATEGORIES = (
        (SOUP, _('Soup')),
        (SALAD, _('Salad')),
        (MAIN_DISH, _('Main Dish')),
        (DESSERT, _('Dessert')),
        (BEVERAGE, _('Beverage')),
    )



    name = models.CharField(max_length=100, blank=False, help_text=_('Name of the item, ie.Barbaque Beef'))
    description = models.TextField(max_length=140, blank=True, help_text=_('Short Item description ie. Short ribs, olive oil, caraway seeds, yoghurt, carrots, onions, white cabbage '))
    price = models.IntegerField(blank=False, help_text=_('Item price ie. 700'))

#    vegeterian = models.BooleanField(default=False, help_text=_('Is vegeterian approved?')) # Vegeterian Approved
#    halal = models.BooleanField(default=False, help_text=_('Is halal approved?')) # Halal Approved
#    vegan = models.BooleanField(default=False, help_text=('Is vegan approved?')) # Vegan Approved
    image = models.ImageField(upload_to='images', blank=True)
#    category = models.CharField(choices=ITEM_CATEGORIES, max_length=50)
    restaurant = models.ForeignKey(RestaurantProfile, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'restaurant', )
        ordering = ('created', )


class TableReserve(CM):
    customer = models.ForeignKey(ClientProfile, on_delete=models.CASCADE, related_name='reservations')
    restaurant = models.ForeignKey(RestaurantProfile, on_delete=models.CASCADE, related_name='reservations')
    no_of_seats = models.IntegerField(help_text=_('No of seats.'))

    def __str__(self):
        return f"Reservation at {self.restaurant.name} on {self.created} for {self.no_of_seats}"

    class Meta:
        ordering = ('created', )
