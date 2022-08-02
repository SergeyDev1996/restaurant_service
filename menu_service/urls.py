from django.urls import path, include
from rest_framework import routers

from menu_service.views import DishViewSet, DrinkViewSet, MenuViewSet, RestaurantViewSet, GetCurrentMenuViewSet


router = routers.DefaultRouter()
router.register("dishes", DishViewSet)
router.register("drinks", DrinkViewSet)
router.register("menu", MenuViewSet)
router.register("restaurants", RestaurantViewSet)
router.register("getting_current_menu", GetCurrentMenuViewSet)
urlpatterns = [path("", include(router.urls))]

app_name = "menu_service"
