from distutils.command.clean import clean
import re
from urllib import request
from django import forms
from .models import MyUser


class RegistrationForm(forms.ModelForm):
    
    cpassword=forms.CharField(max_length=40,widget=forms.PasswordInput,label='Confirm Password')
    def clean_cpassword(self):
            cleaned_data = super().clean()
            p = cleaned_data['password']
            cp = cleaned_data['cpassword']
            print(p,cp)
            if p != cp:
                raise forms.ValidationError('Password And Confirm Password Do Not Match')
            return cp
    def clean_username(self):
            username = self.cleaned_data['username']
            if not re.match(r'^[A-Za-z0-9_]+$', username):
                raise forms.ValidationError("Enter Valid Username")
            return username
    def clean_password(self):
            password = self.cleaned_data['password']
            messg = [
            lambda password: any(x.isupper() for x in password) or 'String must have 1 upper case character.',
            lambda password: any(x.islower() for x in password) or 'String must have 1 lower case character.',
            lambda password: any(x.isdigit() for x in password) or 'String must have 1 number.',
            lambda password: len(password) >= 7                 or 'String length should be atleast 8.',]
            result = [x for x in [i(password) for i in messg] if x != True]
            if result:
                raise forms.ValidationError(result)
            return password  
              
    def clean_fname(self):
            fname = self.cleaned_data['fname']
            if not re.match(r'^[A-Za-z]+$', fname):
                raise forms.ValidationError("Enter Valid First Name")
            return fname

    def clean_lname(self):
            lname = self.cleaned_data['lname']
            if not re.match(r'^[A-Za-z]+$', lname):
                raise forms.ValidationError("Enter Valid Last Name")
            return lname

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',email):
    #         raise forms.ValidationError("Enter A Valid Email Address")
    #     return email
    class Meta:
        model = MyUser
        fields = ['username','fname','lname','email','password','cpassword']
        labels = {'username':'Username','fname':'First Name','lname':'Last Name','email':'Email','password':'Password','cpassword':'ConfirmPassword'}
        widgets = {'password':forms.PasswordInput}
    


        
        
        error_messages = {

            'username': {
                'required': ("This Field Shouldn't Be Empty"),
            },
            'fname': {
                'required': ("This Field Shouldn't Be Empty"),
            },
            'lname': {
                'required': ("This Field Shouldn't Be Empty"),
            },
            'email': {
                'invalid': ("Enter A Valid Email Address"),
            },
            'password': {
                'required': ("This Field Shouldn't Be Empty"),
            },
         
    
        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)