from django.shortcuts import render
from .models import PersonalInfo, slider
# Create your views here.


def home(request):
    data = PersonalInfo.objects.all()
    data2 = slider.objects.all()
    return render(request, "home.html", {"personal_info": data, "slider": data2})
