from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("placeholder to later display list of all blogs")
# Create your views here.

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
