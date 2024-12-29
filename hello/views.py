from django.shortcuts import render
from .models import student

def index(request):
    res = student.objects.all()
    return render(request,"index.html",{'data':res})