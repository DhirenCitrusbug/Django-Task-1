import re
from django.shortcuts import render,redirect
from django.views import View
from .models import MyUser
from .forms import LoginForm, RegistrationForm
from django.contrib.auth.views import LoginView,PasswordChangeView,PasswordResetView,PasswordResetConfirmView,PasswordResetCompleteView
from django.views.generic import ListView,UpdateView,DetailView,DeleteView
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
# from django.contrib.auth import authenticate,login,logout
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
            username = form.cleaned_data['username']
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = MyUser.objects.create_user(username=username,fname=fname,lname=lname,email=email,password=password)
            user.save()
            return render(request,'index.html')
        else:
            return render(request,'signup.html',{'form':form})

class UserList(ListView):
    model = MyUser
    template_name = 'user_list.html'

class UserDetail(DetailView):
    model = MyUser
    template_name = 'user_detail.html'

class UserUpdate(UpdateView):
    form_class = UserChangeForm
    template_name = 'user_update.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user


class UserDelete(DeleteView):
    model = MyUser
    template_name = 'index.html'
    success_url = reverse_lazy('user_list')



class MyLoginView(LoginView):
    template_name='login.html'


class MyPasswordChangeView(PasswordChangeView):
    template_name='change_password.html'
    success_url = '/app1/logout'

class MyPasswordResetView(PasswordResetView):
    template_name='password_reset.html'
    success_url = '/app1/password_reset_confirm'

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name='password_reset_confirm.html'



class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name='password_reset_confirm.html'




[[[[[[[[[]]]]]]]]]












# class Login(View):
#     def get(self,request):
#         form = LoginForm()
#         return render(request,'login.html',{'form':form})
#     def post(self,request):
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request,username=username, password=password)
            
#             if user is not None:
#                 login(request, user)
#                 return render(request,'index.html')
#             else:
#                 print(form.cleaned_data)
#                 return render(request,'login.html',{'form':form})
#         else:
#             return render(request,'login.html',{'form':form})

# class Logout(View):
#     def get(self,request):
#         logout(request)
#         return redirect('login')


