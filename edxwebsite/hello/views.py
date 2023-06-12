
from django.http import HttpResponse
from django.shortcuts import render

# # Create your views here.
# def index(request):
#     return HttpResponse('Welcome to the world of Django')

# def ade(request):
#     return HttpResponse('Hello Ade!')


# def greet(request, name):
#     return HttpResponse(f'Hello {name.capitalize()}!')

# rendering

def index(request):
    return render(request, 'hello/index.html')

def ade(request):
    return HttpResponse('Hello Ade!')


def greet(request, name):
    return render(request, 'hello/greet.html', {
        'name': name.capitalize()
    })
    