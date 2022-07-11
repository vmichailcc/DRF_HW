from django.contrib import admin
from django.urls import path, include
from store.views import hello_world, today, my_name, calculator, StoreApiView
from store.urls import router as store_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello_world/', hello_world),
    path('today/', today),
    path('calculator/', calculator),
    path('store/', StoreApiView.as_view()),
    path('stores/', include(store_router.urls)),
    path('<str:name_of_hacker>/', my_name),
]
