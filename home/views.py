from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def accounthp(request):
    return render(request,'home/accounthp.html',{'user':request.user})