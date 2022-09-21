from django import forms
from .models import MyUser

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username','fname','lname','email','password']
        labels = {'username':'Username','fname':'First Name','lname':'Last Name','email':'Email','password':'Password'}
        widgets = {'password':forms.PasswordInput}


        # error_messages = {
        #     'fname': {
        #         'required': ("This Field is Required"),
        #     },
        #     'lname': {
        #         'required': ("This Field is Required"),
        #     },
        #     'email': {
        #         'required': ("This Field is Required"),
        #     },
        #     'password': {
        #         'required': ("This Field is Required"),
        #     },
    
        # }