from django.shortcuts import render
from smartnetwork import user_settings
from django.shortcuts import HttpResponse
# Create your views here.

def Home(request):
    uContext = {'nav':user_settings.NAV,'sidebar':user_settings.SECTION_NAV,'section_nav':user_settings.SECTION_NAV}


    return render(request,'index.html',uContext)
