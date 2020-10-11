from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Photos


# Create your views here.
def home(request):
    return render(request,'home.html')


def photos(request):
    photo = Photos.objects.all()
    return render(request, 'photo.html', {"photo" : photo})




