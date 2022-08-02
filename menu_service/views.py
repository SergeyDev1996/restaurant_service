from datetime import date
from rest_framework.mixins import ListModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from menu_service.permissions import IsAdminOrIfAuthenticatedReadOnly
from menu_service.models import (
    Dish,
    Drink,
    Restaurant,
    Menu,
    CurrentDayMenu
)
from menu_service.serializers import (
    DishSerializer,
    DrinkSerializer,
    RestaurantSerializer,
    MenuSerializer,
    GetCurrentMenuSerializer,
    RestaurantListSerializer
)


class OrderPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class DishViewSet(ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)
    pagination_class = OrderPagination


class DrinkViewSet(ModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)
    pagination_class = OrderPagination


class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all().prefetch_related(
        "dishes", "drinks"
    )
    serializer_class = MenuSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all().prefetch_related(
        "menu__dishes", "menu__drinks"
    )
    serializer_class = RestaurantSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)
    pagination_class = OrderPagination

    def get_serializer_class(self):
        if self.action == "list":
            return RestaurantListSerializer

        return RestaurantSerializer


today = date.today().strftime("%Y-%m-%d")


class GetCurrentMenuViewSet(ListModelMixin, GenericViewSet):
    queryset = CurrentDayMenu.objects.filter(
        datetime=today).select_related("restaurant", "menu")
    serializer_class = GetCurrentMenuSerializer
    permission_classes = (IsAuthenticated,)

