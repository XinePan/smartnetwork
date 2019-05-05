from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def Home(request):
    uContext = {}
    uContext['menus'] = [{'left':[{'endpoint':'Home','text':'Home','submenu':[{'endpoint':'Home','text':'Home'}]}]}]
    return render(request,'index.html',uContext)
