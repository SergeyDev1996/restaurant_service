from django.contrib import admin

from menu_service.models import (
    Dish,
    Drink,
    Menu,
    Restaurant,
    RestaurantLike,
    CurrentDayMenu
)

admin.site.register(Dish)
admin.site.register(Drink)
admin.site.register(Menu)
admin.site.register(Restaurant)
admin.site.register(RestaurantLike)
admin.site.register(CurrentDayMenu)
