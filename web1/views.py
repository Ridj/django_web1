from django.shortcuts import render

def index(request):
    """The home page for Web1"""
    return render(request, 'web1/index.html')
