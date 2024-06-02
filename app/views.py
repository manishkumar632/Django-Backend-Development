from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    if request.method == "POST":
        # words = request.POST.get('text', '')
        words = request.POST['text']
        no_of_words = len(words.split())
        return render(request, 'index.html', {'no_of_words': no_of_words, 'text': words})
    else:
        return render(request, 'index.html')


def countword(request):
    return render(request, 'countword.html')


def about(request):
    return render(request, 'about.html')