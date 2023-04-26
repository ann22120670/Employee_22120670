# my_library.py

from django.shortcuts import render

def my_contactus(request):
    return render(request, "emp/contactus.html", {})
