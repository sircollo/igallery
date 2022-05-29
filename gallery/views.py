from django.shortcuts import render,Http404
from .models import *

# Create your views here.
def home(request):
    images = Image.objects.all()
    return render(request, 'index.html',{'images':images})