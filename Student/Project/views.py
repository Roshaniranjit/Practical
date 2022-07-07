from django.shortcuts import render
from .models import Student
def base(request):
    context ={
        'students' : Student.objects.all()
    }
    return render(request,'base.html',context)

def index(request,id):
    context ={
        'student' : Student.objects.get(id=1)
    }
    return render(request,'index.html', context)

