from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from .forms import RegisterForm
# Create your views here.


def loginpage(request): 

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username = username  , password = password)

        if user is not None:
            login(request , user)
            return redirect('/')

    
    return render(request , 'login.html' ,)


def logoutpage(request):
        logout(request)
        return redirect('login')



def register(request):

    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect ('/')


    context={'form' : form}
    return render (request , 'register.html' , context)        