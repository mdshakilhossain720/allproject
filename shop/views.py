from django.shortcuts import render
from . forms import StudentRewgestion
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def showforms(request):
    if request.method == 'POST':
       frm=StudentRewgestion(request.POST)
       if frm.is_valid():
          frm.save()
          return HttpResponseRedirect('/successfull/')
    else:
       frm=StudentRewgestion()
       frm.order_fields(field_order=['email','first_name','last_name','batch'])
    return render(request,'form.html',{'form':frm})




def success(request):
   return render(request,'success.html')


def usercform(request):
   frm=UserCreationForm()
   return render(request,'userform.html',{'form':frm})


def login_form(request):
   if request.method =='POST':
      frm=AuthenticationForm(request=request,data=request.POST)
      if frm.is_valid():
         uname=frm.cleaned_data['username']
         upass=frm.cleaned_data['password']
         user=authenticate(username=uname,password=upass)
         if user is not None:
            login(request,user)
            return HttpResponseRedirect('successfull')
        
   else:
        frm=AuthenticationForm()
   return render(request,'login.html',{'from':frm})

def slogin(request):
   return render(request,'slogin.html')

def log_out(request):
   logout(request)
   return HttpResponseRedirect('successfull')




