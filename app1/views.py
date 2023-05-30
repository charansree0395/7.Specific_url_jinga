from django.shortcuts import render

# Create your views here.

def first(request):
    d={'name':'Sai Reddy','age':23,'location':'kavali'}
    return render(request,'first.htm',d)