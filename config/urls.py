"""
URL configuration for tara_libot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from tara_libot_web_client.versions.v1p0.features.maps.create_maps.views import create_map_view
from tara_libot_web_client.versions.v1p0.features.maps.display_maps.views import display_map_view
from tara_libot_web_client.versions.v1p0.features.maps.delete_maps.views import delete_map_view
from tara_libot_web_client.versions.v1p0.features.maps.update_maps.views import update_map_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('marker/create/', create_map_view.MarkerListCreateView.as_view()),
    path('marker/get/', display_map_view.MarkerListDisplayView.as_view()),
    path('marker/delete/', delete_map_view.MarkerListDeleteView.as_view()),
    path('marker/update/', update_map_view.MarkerListUpdateView.as_view()),
]
