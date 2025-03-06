from django.http import HttpResponse
from django.shortcuts import render

from db_articles import articles

def home_view(request):
    # return HttpResponse("hello word")
    return render(request, 'index.html')

def contact_view(request):
        # return HttpResponse("contact")
        return render(request, 'contact.html')

def articles_view(request):
    return render(request, 'articles.html', context={'articles': articles})

def Apropos_view(request):
    return render(request, 'A propos.html' )






