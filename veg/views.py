from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def fryrice(request):
    return HttpResponse("<h1><i>*mushroom fry*</i><h1/>")
def zomato(request):
    return render(request,'zomato.html')
