from django.shortcuts import render
from .models import Stations

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def about(request):
    return render(request,'about.html')

def department(request,):
    dep=Stations.objects.all()
    context={
        'dep':dep
    }
    return render(request,'departments.html',context)


def department_detail(request,id):
    detail=Stations.objects.get(id=id)
    context={
        'detail':detail
    }
    return render(request,'department_detail.html',context)

def gallery(request):
    return render(request,'gallery.html')

def news(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def members(request):
    return render(request,'team.html')

def survival_view(request):
    return render(request, 'survivals.html')


def staff(request):
    return render(request, 'staff.html')