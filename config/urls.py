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
from tara_libot_web_client.versions.v1p0.features.login.views.login_views import LoginAdminView
from tara_libot_web_client.versions.v1p0.features.logout.views.logout_views import LogoutAdminView
from tara_libot_web_client.versions.v1p0.features.add_review_restaurant.views.add_review_restaurant_views import AddReview
from tara_libot_web_client.versions.v1p0.features.display_review_restaurant.views.display_reviews_restaurant_views import DisplayRestaurantDetailReview, DisplayRestaurantReview, RestaurantReviewListAPIView
from tara_libot_web_client.versions.v1p0.features.add_food_review_restaurant.views.add_food_review_views import AddFoodReview
from tara_libot_web_client.versions.v1p0.features.display_food_review_restaurant.views.display_food_review_views import DisplayFoodDetailReview, DisplayFoodRestaurantReview, FoodReviewListAPIView
from tara_libot_web_client.versions.v1p0.features.like_and_unlike_review_restaurant.views.like_and_unlike_views import LikeAndUnlikeView
from tara_libot_web_client.versions.v1p0.features.like_and_unlike_reviews_food.views.like_and_unlike_food_views import LikeAndUnlikeFoodView
from tara_libot_web_client.versions.v1p0.features.display_food_review_restaturant_kiosk.views.kiosk_food_review_views import KioskFoodReviewListAPIView, DisplayFoodDetailKioskReview
from tara_libot_web_client.versions.v1p0.features.display_review_restaurant_kiosk.views.display_restaurant_review_kiosk_views import RestaurantReviewKioskListsAPIView, DisplayRestaurantKioskDetailReview
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/v1p0/', LoginAdminView.as_view(), name = "login"),
    path('logout/v1p0/',LogoutAdminView.as_view(), name = "logout"),
    path ('review/restaurant/<pk>/add/', AddReview.as_view(), name ="add_review"),
    path ('review/restaurant/<pk>/get/', DisplayRestaurantDetailReview.as_view(),name ="get_review_restaurant_detail"),
    path ('review/restaurant/get/', DisplayRestaurantReview.as_view(), name= "get_review_all_restaurant"),
    path ('review/food/<pk>/add/', AddFoodReview.as_view(), name = "add_food_review"),
    path ('review/food/get/', DisplayFoodRestaurantReview.as_view(), name = "get_food_review"),
    path ('review/food/<pk>/get/', DisplayFoodDetailReview.as_view(), name = "get_food_detail_review"),
    path('restaurant/<int:restaurant_id>/reviews/', RestaurantReviewListAPIView.as_view(), name='restaurant_review_list'),
    path('food/<int:food_id>/reviews/',FoodReviewListAPIView.as_view(), name="food_restaurant_review_list"),
    path('review/comments/<pk>/add/likes/', LikeAndUnlikeView.as_view(), name = "like_and_unlike_restaurant"),
    path('review/food/comments/<pk>/add/likes/', LikeAndUnlikeFoodView.as_view(), name = "like_and_unlike_restaurant"),
    path('kiosk/food/review/get/<int:food_id>/', KioskFoodReviewListAPIView.as_view(), name = 'kiosk_food_restaurant_review_list' ),
    path('kiosk/food/review/get/review/<pk>/', DisplayFoodDetailKioskReview.as_view(), name = 'kiosk_food_restaurant_review_list' ),
    path('kiosk/restaurant/get/<int:restaurant_id>/', RestaurantReviewKioskListsAPIView.as_view(), name = 'kiosk_restaurant_review_list'),
    path('kiosk/restaurant/review/get/<pk>/',DisplayRestaurantKioskDetailReview.as_view(), name = 'kiosk_restaurant_review_detail')
    
]
