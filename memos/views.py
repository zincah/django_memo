from django.shortcuts import redirect, render
from .models import Memos

# Create your views here.

def index(request):
    mo = Memos.objects.all()
    context = {
        "memos" : mo
    }
    return render(request, "memos/index.html", context)

def add(request):
    if request.method == "POST":
        sub = request.POST.get("subject")
        wri = request.POST.get("writer")
        con = request.POST.get("content")
        mo = Memos(subject=sub, writer=wri, content=con)
        mo.save()
        return redirect("memos:index")

    return render(request, "memos/add.html")

def detail(request, mpk):
    mo = Memos.objects.get(id=mpk)
    context = {
        "memos" : mo,
    }
    return render(request, "memos/detail.html", context)

def modify(request, mpk):
    mo = Memos.objects.get(id=mpk)
    context = {
        "memos" : mo
    }
    if request.method == "POST":
        con = request.POST.get("content")
        mo.content = con
        mo.save()
        return redirect("memos:detail", mpk=mpk)
    return render(request, "memos/modify.html", context)