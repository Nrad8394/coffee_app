from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .EmailBackEnd import EmailBackEnd


# Create your views here.

def index(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')

def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user != None:
            login(request, user)
            user_type = user.user_type 
            #return HttpResponse("Email: "+request.POST.get('email')+ " Password: "+request.POST.get('password'))
            if user_type == '1':
                return redirect('admin_dashboard')
                
            elif user_type == '2':
                # return HttpResponse("Clerk Login")
                return redirect('clerk_home')
                
            elif user_type == '3':
                # return HttpResponse("Supplier Login")
                return redirect('supplier_home')
            else:
                messages.error(request, "Invalid Login!")