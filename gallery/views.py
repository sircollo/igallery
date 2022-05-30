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
    
DoesNotExist = False  
def filter_location(request,location_id):
    try:
        locations = {'1':"Moscow",'2':"Tokyo",'3':"Cairo",'4':"Nairobi",'5':"England",'6':"China"}    
        filtered_images = Image.objects.filter(location__name__icontains=locations.get(str(location_id))) 
        message = f"{locations.get(location_id)}"
    except  DoesNotExist:
         raise Http404()
    return render(request,'locations.html',{"message":message,"images": filtered_images})

