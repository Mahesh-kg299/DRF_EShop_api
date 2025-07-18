from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import (
    UserCreateAPIView,
    BrandViewSet,
    CategoryViewSet,
    SubCategoryViewSet,
    LoginAPIView,
    ProductViewSet,
    LogOutAPIView
)


router = DefaultRouter()
router.register(r'brands', BrandViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'sub_categories', SubCategoryViewSet)
router.register(r'products', ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserCreateAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('get_api_token/', views.obtain_auth_token),
    path('logout/', LogOutAPIView.as_view()),
]