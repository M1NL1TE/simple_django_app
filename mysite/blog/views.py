from django.http import HttpResponse 

# Create your views here.

def index(requests):
    return HttpResponse("Hello, this is my first django app")