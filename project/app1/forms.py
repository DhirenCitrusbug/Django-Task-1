from django import forms
from .models import MyUser
from django.contrib.auth.forms import AuthenticationForm,UsernameField,PasswordChangeForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
import re
class RegistrationForm(forms.ModelForm):
    
    cpassword=forms.CharField(max_length=40,widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Confirm Password')
    def clean_cpassword(self):
            cleaned_data = super().clean()
            p = cleaned_data.get('password')
            cp = cleaned_data.get('cpassword')
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
        widgets = {
        'username':forms.TextInput(attrs={'class':'form-control'}),
        'fname':forms.TextInput(attrs={'class':'form-control'}),
        'lname':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        'password':forms.PasswordInput(attrs={'class':'form-control'}),}
    


        
        
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

class LoginForm(AuthenticationForm):
    
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True,'class':'form-control'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",'class':'form-control'}),
    )


class MySetPasswordForm(forms.Form):
    """
    A form that lets a user change set their password without entering the old
    password
    """

    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
    }
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control'}),
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get("new_password1")
        password2 = self.cleaned_data.get("new_password2")
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages["password_mismatch"],
                    code="password_mismatch",
                )
        password_validation.validate_password(password2, self.user)
        return password2

class MyPasswordChangeForm(MySetPasswordForm):
    """
    A form that lets a user change their password by entering their old
    password.
    """

    error_messages = {
        **MySetPasswordForm.error_messages,
        "password_incorrect": _(
            "Your old password was entered incorrectly. Please enter it again."
        ),
    }
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True,'class':'form-control'}
        ),
    )

    field_order = ["old_password", "new_password1", "new_password2"]

    def clean_old_password(self):
        """
        Validate that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                self.error_messages["password_incorrect"],
                code="password_incorrect",
            )
        return old_password