from django.shortcuts import render, redirect
from . models import query

def func(request):
    if request.method=="POST":
        id=request.POST.get("id")
        ans = query.objects.get(id=id)
        if ans is None:
            return render(request,"index.html",{})
        else:
            return render (request,"ans.html",{'ans':ans})

def index(request):
    return render(request,"index.html",{})