from django.shortcuts import render

def home(request):
    print(request.is_secure())
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')