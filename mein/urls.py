from django.urls import path # type: ignore

from .views import index

urlpatterns = [
    path('', index,name='index'),
    
]