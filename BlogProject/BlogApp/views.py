from django.shortcuts import render
from django.http import HttpResponse
from .models import post
import time

# Create your views here.
def home(request):
    posts = post.objects.all()
    return render(request,"index.html",{'posts':posts})
def postpage(request, ID):
    page = post.objects.get(id=ID)
    return render(request, 'post.html', {'page':page})
def create(request):
    
    if request.method == "GET":
     return render(request,"create.html")
    elif request.method == "POST":
       new_post = request.POST.get("postcreated")
       new_title = request.POST.get("newtitle")
       writer = request.POST.get("writer")
       new_time = time.strftime("%H %M %S", time.localtime())
       post.objects.create(title=new_title, content=new_post, author=writer, time = new_time)
    