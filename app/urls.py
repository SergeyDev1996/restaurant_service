from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/menu_service/", include("menu_service.urls", namespace="menu_service")),
    path("api/user/", include("user.urls", namespace="user")),
]
