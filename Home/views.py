from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def Home(request):
    uContext = {}
    uContext['nav'] = [{'endpoint':'home','text':'Home'}]
    uContext['sidebar'] = [{'endpoint': '#header', 'text': '概览'}]
    return render(request,'index.html',uContext)
