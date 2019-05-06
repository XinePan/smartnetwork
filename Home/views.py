from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def Home(request):
    uContext = {}
    uContext['menus'] = [{'left':[{'id':'Home','endpoint':'Home','text':'Home',},{'id':'Home','endpoint':'Home','text':'Home','submenu':[{'id':'Home1','endpoint':'Home','text':'Home'},{'id':'Home2','endpoint':'Home','text':'Home'}]}]}]
    return render(request,'index.html',uContext)
