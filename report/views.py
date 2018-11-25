from django.shortcuts import render, redirect, HttpResponse
from . models import query
import requests
from django.http import FileResponse, HttpResponseRedirect
from . forms import Form


def index(request):
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            id=request.POST.get("id")
            ans = query.objects.get(id=id)
            response=ans.repo.url
            if ans is None:
                return redirect("index.html")
            else:
                #return render (request,"ans.html",{'ans':response})
                return redirect(response)
    else:
        form = Form()
    return render(request,"index.html",{'form':form})