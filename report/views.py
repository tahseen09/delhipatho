from django.shortcuts import render, redirect, HttpResponse
from . models import query
import requests
from django.http import FileResponse

def func(request):
    if request.method=="POST":
        id=request.POST.get("id")
        ans = query.objects.get(id=id)
        response=ans.repo
        if ans is None:
            return redirect("index.html")
        else:
            """return render (request,"ans.html",{'ans':response})"""
            return redirect(response)
def index(request):
    return render(request,"index.html",{})