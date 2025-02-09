<<<<<<< HEAD
from django.urls import path # type: ignore

from .views import index

urlpatterns = [
    path('', index,name='index'),
    
]
=======
from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('', Index_View.as_view(),name='index'),
    path('trainer/', Trainer_View.as_view(),name='trainer'),
    path('why/', Why_View.as_view(),name='why'),
    path('contact', Contact_View.as_view(),name='contact'),
    path('keraksiz/', keraksiz,name='keraksiz'),

]
>>>>>>> 0984425 (1-commit)
