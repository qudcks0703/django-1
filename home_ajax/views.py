from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import json
# Create your views here.
def ajax1(request):
    return render(request,"ajax1.html")
def ajax1_basic(request):
    context={'msg':'hello'}
    return JsonResponse(context)