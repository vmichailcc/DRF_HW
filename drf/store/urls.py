from django.urls import path, include
from rest_framework import routers
from .views import StoreViewSet


router = routers.SimpleRouter()
router.register('', StoreViewSet, basename='stores')

