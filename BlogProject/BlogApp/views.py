from django.shortcuts import render
from django.http import HttpResponse
from .models import post
from datetime import datetime
import random

# Create your views here.
techimglist = ["tech1", "tech2", "tech3", "tech4", "tech5", "tech6"]
busimglist = ["bus1", "bus2", "bus3", "bus4"]
lifeimglist = ["life1", "life2", "life3", "life4", "life5"]
healimglist = ["heal1", "heal2", "heal3", "heal4", "heal5", "heal6"]
entimglist = ["ent1", "ent2", "ent3", "ent4"]
eduimglist = ["edu1", "edu2", "edu3"]
foodimglist = ["food1", "food2", "food3", "food4"]


def index(request):
    """Homepage - display all posts"""
    posts = post.objects.all()
    imgname = "postimg"
    return render(request, "index.html", {'posts': posts, 'imgname': imgname})


def post_full(request, post_id):
    """Display full post detail page"""
    page = post.objects.get(id=post_id)
    return render(request, 'post.html', {'page': page})


def create(request):
    """Create a new post - GET shows form, POST saves post"""
    if request.method == "GET":
        return render(request, "create.html")
    
    elif request.method == "POST":
        new_post = request.POST.get("postcreated")
        new_title = request.POST.get("newtitle")
        writer = request.POST.get("writer")
        time_made = datetime.now()
        tagname = request.POST.get("tag")
        
        # Select random image based on category
        if tagname == "tech":
            imgname = random.choice(techimglist)
        elif tagname == "bus":
            imgname = random.choice(busimglist)
        elif tagname == "life":
            imgname = random.choice(lifeimglist)
        elif tagname == "heal":
            imgname = random.choice(healimglist)
        elif tagname == "ent":
            imgname = random.choice(entimglist)
        elif tagname == "edu":
            imgname = random.choice(eduimglist)
        elif tagname == "food":
            imgname = random.choice(foodimglist)
        else:
            imgname = "default"

        # Create the post
        new_post = post.objects.create(
            title=new_title, 
            content=new_post,
            author=writer, 
            time=time_made, 
            picture=imgname + ".jpg",
            tag=tagname
        )
        
        # Redirect to success page
        return render(request, "ready.html", {'post_id': new_post.id})


def ready(request, post_id):
    """Success page after posting"""
    try:
        new_post = post.objects.get(id=post_id)
        return render(request, "ready.html", {'post': new_post, 'post_id': post_id})
    except post.DoesNotExist:
        return render(request, "ready.html", {'post_id': post_id})
