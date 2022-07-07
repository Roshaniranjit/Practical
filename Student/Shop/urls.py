from django.urls import path
from .views import shopbase,shopindex
urlpatterns = [
    path('shopbase/',shopbase ,name ="shopbase"),
    path('shopindex/<int:id>', shopindex ,name ='shopindex'),
    
    
]
