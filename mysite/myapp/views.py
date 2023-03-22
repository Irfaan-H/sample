from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home (request):

    return render(request,'home.html')

def add(request):
    val1 =int(request.GET['num1'])
    val2 =int(request.GET['num2'])
    res1= val1 +val2
    return render (request,'home.html',{'result':res1})



    
def sub(request):

    val1=int(request.GET["num1"])
    val2=int(request.GET["num2"])
    res2= val1 - val2
    return render(request,'home.html',{'result':res2})

    
def mul(request):

    val1=int(request.GET['num1'])
    val2=int(request.GET['num2'])
    res3=val1* val2
    return render(request,'home.html',{'result':res3})



def div(request):

    val1=int(request.GET['num1'])
    val2=int(request.GET['num2'])
    res4=val1 / val2 
    return render(request,'home.html',{'result':res4})


   
