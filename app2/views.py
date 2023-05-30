from django.shortcuts import render

# Create your views here.

def second(request):
    d={'name':'sravan','age':24,'location':'ATP'}
    return render(request,'second.html',d)