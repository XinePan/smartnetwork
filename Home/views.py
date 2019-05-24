from django.shortcuts import render
from smartnetwork import user_settings
from django.shortcuts import HttpResponse
# Create your views here.

def Home(request):
    uContext = {'nav':user_settings.NAV,'sidebar':user_settings.SIDEBAR['index'],'section_nav':user_settings.SECTION_NAV['index']}
    return render(request,'index.html',uContext)
