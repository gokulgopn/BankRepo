from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'home.html')
def redirect_idukki(request):
    return redirect("https://en.wikipedia.org/wiki/Idukki_district")
def redirect_kottayam(request):
    return redirect("https://en.wikipedia.org/wiki/Kottayam")
def redirect_malappuram(request):
    return redirect("https://en.wikipedia.org/wiki/Malappuram")
def redirect_palakkad(request):
    return redirect("https://en.wikipedia.org/wiki/Palakkad")
def redirect_kochi(request):
    return redirect("https://en.wikipedia.org/wiki/Kochi")
def login(request):
    return render(request, "login.html")


