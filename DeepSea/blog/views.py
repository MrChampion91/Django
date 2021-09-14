from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "blog/home.html")


def contacti(request):
    return HttpResponse("<h2>contacti_page</h2>")
# Create your views here.
