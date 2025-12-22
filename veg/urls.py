from django.urls import path
from veg.views import *
urlpatterns = [
    path('fryrice/', fryrice, name='fryrice'),
    path('zomato/', zomato, name='zomato'),
]