from django.shortcuts import render
from django.http import HttpResponse


def register(request):
    # return HttpResponse("<h1>Hello Django!</h1>")
    return render(request, "user/register.html")
