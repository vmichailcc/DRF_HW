from django.contrib import admin
from django.urls import path, include
from store.views import hello_world, today, my_name, calculator, StoreApiView
from store.urls import router, my_stores_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello_world/', hello_world),
    path('today/', today),
    path('calculator/', calculator),
    path('store/', StoreApiView.as_view()),
    path('stores/', include(router.urls)),
    path('my_stores/', include(my_stores_router.urls)),
    path('my_name/<str:name_of_hacker>/', my_name),
]
