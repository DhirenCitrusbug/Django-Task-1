from django.shortcuts import render,redirect
from django.views import View
from .models import MyUser
from .forms import RegistrationForm
from django.contrib.auth import authenticate,login
# Create your views here.
class Index(View):
    def get(self,request):
        return render(request,'index.html')

class SignUp(View):
    def get(self,request):
        form = RegistrationForm()
        return render(request,'signup.html',{'form':form})
    def post(self,request):
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            if form.cleaned_data['password']==request.POST['cpassword']:
                username = form.cleaned_data['username']
                fname = form.cleaned_data['fname']
                lname = form.cleaned_data['lname']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                user = MyUser.objects.create(username=username,fname=fname,lname=lname,email=email,password=password)
                user.save()
                return render(request,'login.html')
            else:
                password_err = "Password Didn't match"
                return render(request,'signup.html',{'form':form,'password_err':password_err})
        else:
            return render(request,'signup.html',{'form':form})

class UserDetail(View):
    def get(self,request):
        users = MyUser.objects.all()
        return render(request,'users.html',{'users':users})

class UserUpdate(View):
    def get(self,request,pk):
        user = MyUser.objects.filter(pk=pk)
        return render(request,'user_detail.html',{'user':user})

class Login(View):
    def get(self,request):
        form = RegistrationForm()
        return render(request,'login.html',{'form':form})
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        login(request, user)
        if user:
            return render(request,'index.html')
        else:
            return render(request,'login.html')