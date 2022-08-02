from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status
from menu_service.models import Menu
from menu_service.serializers import MenuSerializer

MENU_URL = reverse("menu_service:menu-list")
RESTAURANT_URL = reverse("menu_service:restaurant-list")


def sample_menu(**params):
    defaults = {
        "about": "Sample menu"
    }
    defaults.update(params)

    return Menu.objects.create(**defaults)


class UnauthenticatedMenuApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(MENU_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class AuthenticatedMenuApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "test@test.com",
            "testpass",
        )
        self.client.force_authenticate(self.user)

    def test_list_menu(self):
        sample_menu()
        res = self.client.get(MENU_URL)

        menus = Menu.objects.all().order_by("id")
        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_menu_forbidden(self):
        payload = {
            "about": "New menu",
        }
        res = self.client.post(MENU_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class AdminMovieApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "admin@admin.com", "testpass", is_staff=True
        )
        self.client.force_authenticate(self.user)

    def test_create_menu(self):
        payload = {
            "about": "Menu",
        }
        res = self.client.post(MENU_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        menu = Menu.objects.get(id=res.data["id"])
        for key in payload.keys():
            self.assertEqual(payload[key], getattr(menu, key))



