from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MyRegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:                                                   #Helps specify the order of display
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)     
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
       
        if commit:
            user.save()

        return user


#Created a custom class from UserCreationForm, kind of inherited the class
#Line 16 -> super lets it call UserCreationForm method save, ignoring its own save method
#setting commit=False prevents it to return user in save method of CreationUserForm
