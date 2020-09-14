from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from accounts.forms import SignupForm,EditProfileInfo
# Create your views here.
def signup_view(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            #login(request,user)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request,'accounts/signup.html',{'form':form})

def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('/')

def profile(request):
    if request.method=='POST':
        form = EditProfileInfo(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile/')
    else:
        form = EditProfileInfo(instance=request.user)
    return render(request,'accounts/profile.html',{'user':request.user,'form':form})