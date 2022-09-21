from distutils.command.clean import clean
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
            if username.isdigit():
                raise forms.ValidationError("Username Can't Be Number")
            return username
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
                'required': ("This Field Shouldn't Be Empty"),
            },
            'password': {
                'required': ("This Field Shouldn't Be Empty"),
            },
         
    
        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)