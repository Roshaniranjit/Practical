from django.shortcuts import render
from .models import Hospital
def hospitalbase(request):
    context ={
        'hospitals' : Hospital.objects.all()
    }
    return render(request,'hospitalbase.html',context)
    
    
    
def hospitalindex(request,id):
    context ={
        'hospital' : Hospital.objects.get(id= id)
    }
    
    return render(request,'hospitalindex.html',context)
