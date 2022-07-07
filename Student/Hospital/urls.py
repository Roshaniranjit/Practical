from django.urls import path
from .views import hospitalbase,hospitalindex

urlpatterns = [
    path('hospitalbase/',hospitalbase ,name ="hospitalbase"),
    path('hospitalindex/<int:id>', hospitalindex ,name ='hospitalindex'),
]