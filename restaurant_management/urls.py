"""restaurant_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny


openapi_info = openapi.Info(
    title="Restaurant management",
    default_version='v1',
    description="All the endpoints of the Restaurant management",
    license=openapi.License(name="All Rights Reserved"),
)

schema_view = get_schema_view(
    openapi_info,
    public=True,
)


urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path("api/v1/users/", include("apps.users.urls"), name="users"),
    path("api/v1/restaurants/", include("apps.restaurants.urls"), name="restaurants"),
    path(
        "api/v1/restaurants/<int:restaurant_id>/", include("apps.menus.urls"),
        name="menus_categories"
    ),
    path(
        "api/v1/restaurants/<int:restaurant_id>/", include("apps.orders.urls"),
        name="orders"
    ),
]
