from django.shortcuts import render, HttpResponse, reverse, redirect
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm


# Create your views here.
def home(request):
    return render(request, 'base.template.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('home'))

def login(request):
    #user clicked on submit
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        #input validation, followed by:
        #authenticate to see if the username and pw matches anything in the database. 
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
            #if there is a user and pw that matches
            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('home'))
            else:
                return redirect(reverse('login'))
    else:
        form = UserLoginForm()
        return render(request, 'accounts/login.html', {
            "form":form
        })

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password2'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request,"You have registered successfully")
            else:
                messages.error(request, "Your registration has failed")
            return redirect(reverse('home'))
        else:
            return redirect(reverse('home'), {
                'form':form
            })
    else:
        form = UserRegistrationForm()
        return render(request, 'accounts/register.template.html',{
            'form':form
        })