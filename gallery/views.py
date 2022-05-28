from django.shortcuts import render,Http404

# Create your views here.
def home(request):
    return render(request, 'index.html')