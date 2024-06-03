from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json


def home(request):
    if len(request.POST) > 0:
        values = list(request.POST.values())[1:]
        if values.count('') > 0:
            return render(request, "index.html", {"data": "Please enter values"})
        values = [int(value) for value in values]
        total = sum(values)
        return render(request, "index.html", {"data": total})
    return render(request, "index.html")

def aboutus(request):
    return render(request, 'aboutus.html')
