from rest_framework import routers
from .views import StoreViewSet, MyStoreModelView, AdminStories


router = routers.SimpleRouter()
router.register('', StoreViewSet, basename='stores')

my_stores_router = routers.SimpleRouter()
my_stores_router.register('', MyStoreModelView, basename='my_stores')

admin_router = routers.SimpleRouter()
admin_router.register('', AdminStories, basename='admin_stores')
