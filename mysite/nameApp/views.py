from django.http import HttpResponse 
from django.shortcuts import render
from .models import Post

# Create your views here.

def index(requests):

    posts = Post.objects.all()
    data = {

   "Name" : "Michael Nwachukwu",

    "Track" : "Backend(Python)",

    "Message" : "Hi, mentor, you're doing a great job!"

}
    return render(requests, "nameApp/index.html", {'data': data})
