from django.shortcuts import render

# Create your views here.
def jinja(request):
    d={'name':'dashrath','age':23, 'state':'MAHARASHTRA'}
    return render(request, 'jinja.html', context=d)

def ifelif(request):
    d={'a':10, 'b':80, 'c': 12}
    return render(request, 'ifelif.html', context=d)

def nestedif(request):
    d={'a':10, 'b':80, 'c': 120}
    return render(request, 'nestedif.html', context=d)