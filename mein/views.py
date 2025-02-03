from django.shortcuts import render # type: ignore
from .models import *




def index(request):
    groups = Group.objects.all()
    return render(request, 'index.html', {'groups':groups})
