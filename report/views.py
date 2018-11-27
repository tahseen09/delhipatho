from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from . models import query
from django.http import FileResponse, HttpResponseRedirect
from . forms import Form


def index(request):
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            id=request.POST.get("id")
            ans = get_object_or_404(query, id=id)
            response=ans.repo.url
            return redirect(response)
    else:
        form = Form()
    return render(request,"index.html",{'form':form})