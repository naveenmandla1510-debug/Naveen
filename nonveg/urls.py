from django.urls import path
from nonveg.views import *
urlpatterns = [
    path('chicken/', chicken, name='chicken'),
    path('zomato/', zomato, name='zomato'),
]