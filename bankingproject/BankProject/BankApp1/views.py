from django.contrib import messages
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    return render(request, "register.html")
def new(request):
    return render(request,"new.html")
def form(request):
    return render(request,"form.html")
def final(request):
    return render(request,"final.html")
