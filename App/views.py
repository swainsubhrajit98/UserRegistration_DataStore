from django.shortcuts import render,HttpResponse
from App.forms import *
# Create your views here.

def UserRegistration(request):
    form=UserForm()
    d={'form':form}
    if request.method=='POST':
        form_data=UserForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('Registration done Successfully!!!')
    return render(request,'UserRegistration.html',d)