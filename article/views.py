from django.shortcuts import render
from django.http import HttpResponse

def article_list(request):
    return HttpResponse("hello world!")
