from django.shortcuts import render
from smartnetwork import user_settings as sys_user_setting
from Home import user_settings
from django.shortcuts import HttpResponse
# Create your views here.

def Home(request):
    uContext = {'nav':sys_user_setting.NAV,'sidebar':user_settings.SIDEBAR['index'],'section_nav':user_settings.SECTION_NAV['index']}
    uContext['carousel']=user_settings.CAROUSEL
    return render(request,'index.html',uContext)
