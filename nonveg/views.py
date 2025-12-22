from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def chicken(request):
    return HttpResponse("*Boneless*,*dum*,*fry*")
def zomato(request):
    return render(request,'zomato.html')