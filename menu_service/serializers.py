from rest_framework import serializers

from menu_service.models import (
    Dish,
    Drink,
    Restaurant,
    Menu,
    CurrentDayMenu
)


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ("id", "name", "info", "price",)


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ("id", "name", "price",)


class MenuSerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True, read_only=False)
    drinks = DrinkSerializer(many=True, read_only=False)

    class Meta:
        model = Menu
        fields = ("id", "about", "dishes", "drinks",)


class RestaurantSerializer(serializers.ModelSerializer):
    likes = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="username"
    )
    menu = MenuSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ("id", "name", "menu", "likes", "count_likes")


class RestaurantListSerializer(serializers.ModelSerializer):
    likes = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="username"
    )
    menu = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="about"
    )

    class Meta:
        model = Restaurant
        fields = ("id", "name", "menu", "likes", "count_likes")


class GetCurrentMenuSerializer(serializers.ModelSerializer):
    restaurant = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field="name"
    )
    likes = RestaurantSerializer(
        source="count_likes", read_only=True
                                 )
    menu = MenuSerializer(many=False, read_only=True)

    class Meta:
        model = CurrentDayMenu
        fields = ("datetime", "menu", "restaurant", "likes", )

