from django.db import models

from app import settings


class Dish(models.Model):
    name = models.CharField(max_length=63)
    info = models.CharField(max_length=255)
    price = models.IntegerField()

    class Meta:
        verbose_name_plural = "Dishes"

    def __str__(self):
        return str(self.name)


class Drink(models.Model):
    name = models.CharField(max_length=63)
    price = models.IntegerField()

    def __str__(self):
        return str(self.name)


class Menu(models.Model):
    about = models.CharField(max_length=255)
    dishes = models.ManyToManyField(Dish, related_name="dishes")
    drinks = models.ManyToManyField(Drink, related_name="drinks")

    def __str__(self):
        return str(self.about)


class Restaurant(models.Model):
    name = models.CharField(max_length=63)
    info = models.CharField(max_length=255)
    menu = models.ManyToManyField(Menu)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through="RestaurantLike"
    )

    @property
    def count_likes(self) -> int:
        return self.likes.count()

    def __str__(self):
        return str(self.name)


class RestaurantLike(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE
    )


class CurrentDayMenu(models.Model):
    datetime = models.DateField(auto_created=True)
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE
    )
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-datetime"]
