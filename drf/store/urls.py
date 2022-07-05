from django.urls import path
from .views import hello_world, today, my_name, calculator

urlpatterns = [
    path('hello_world/', hello_world),
    path('today/', today),
    path('calculator/', calculator),
    path('<str:name_of_hacker>/', my_name),
]
