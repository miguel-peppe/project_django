from django.shortcuts import render

# Create your views here.


def start(request):
    return render(request, 'modulos/pages/index.html', context={
        'name': 'Code Crafters'
    })


def dashboard(request):
    return render(request, 'temp.html')
