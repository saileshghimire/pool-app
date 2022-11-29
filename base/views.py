from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
def index(request):
    
    data = {}
    q = Party.objects.all()
    if request.method == "POST":
        content = request.POST
        if content in q.title :
            q.count+=1
            q.save()
            return render(request,'message.html',data)
    return render(request, 'index.html',data)

 
    