from django.shortcuts import render
from .models import Shop
# Create your views here.


def shopbase(request):
    context = {
        'shops' : Shop.objects.all()
    }
    return render(request,'shopbase.html',context)

def shopindex(request,id):
    context = {
        'shop' : Shop.objects.get(id=id)
    }
    return render(request,'shopindex.html')
