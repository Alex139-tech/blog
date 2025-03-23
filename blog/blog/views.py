# blog_app/views.py
from django.shortcuts import render,HttpResponse
from .models import Post

def home(request):
 return render(request,"base.html")
