from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    # return HttpResponse("This is homepage")
    context={
        'variable1':"this is sent",
        'variable2':"this is a test Django project."
    }
    # messages.success(request, "this is a test message")
    return render(request,'index.html')
def about(request):
    # return HttpResponse("This is about page")
    return render(request,'about.html')
def services(request):
    # return HttpResponse("This is about contact page")
    return render(request,'services.html')
def contact(request):
    # return HttpResponse("This is services page")
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()

        messages.success(request,'Your message has been sent!')
  
    return render(request,'contact.html')