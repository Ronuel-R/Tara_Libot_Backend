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
from django.urls import path , re_path
from tara_libot_web_client.versions.v1p0.features.landing_page_kiosk.views import landing_page_kiosk_view
from tara_libot_web_client.versions.v1p0.features.business_page_kiosk.views import business_page_kiosk_views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path("home/kiosk/", landing_page_kiosk_view.LandingPageKiosk.as_view()),
    re_path("home/business/", business_page_kiosk_views.BusinessKioskViews.as_view()),
]
