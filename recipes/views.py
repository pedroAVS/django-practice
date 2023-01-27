from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Pedro',
    })


def temp(request):
    return render(request, 'temp.html')
