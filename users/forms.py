from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,Permission,Group
from  django import forms
import re


# class registerform(UserCreationForm):
#     class Meta:
#         model = User
#         fields=       ['username','first_name','last_name','password1','password2','email']
#     def __init__(self, *args, **kwargs):
#         super(UserCreationForm,self).__init__(*args, **kwargs)

#         for fieldname in ['username','password1','password2']:
#             self.fields[fieldname].help_text=None
    
class coustomregistrationform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields =   ['username','first_name','last_name','password','confirm_password','email']
       

    def clean_password(self):
        password = self.cleaned_data.get('password')
        errors = []
        if len(password)<8:
            errors.append("Password must be 8 character long")
        if not "abc" in password:
            errors.append("Not abc in password")
        if errors:
            raise forms.ValidationError(errors)
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password =cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Confirm password not match")
        
        return  cleaned_data 


class Assignroleform(forms.Form):
    role = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        empty_label="Selet a Role"
    )

class creategroupform(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required = False,
        label = "Assign permission"
       )
    class Meta:
        model = Group
        fields=['name','permissions']



        
