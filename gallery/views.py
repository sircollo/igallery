from django.shortcuts import render,Http404
from .models import *

# Create your views here.
def home(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    return render(request, 'index.html',{'images':images,'locations':locations})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
