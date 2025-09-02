from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello Django!</h1>")

def contact(request):
    return HttpResponse("<h1>Contact us</h1>")

def about(request):
    return HttpResponse("<h1>About us</h1>")
