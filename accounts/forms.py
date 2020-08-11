from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class ChangeUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'mobile_number']

        widgets = {
            'email': forms.TextInput(attrs={'readonly': 'readonly'}),
            'mobile_number': forms.TextInput(attrs={'readonly': 'readonly'}),
        }


class ChangeUserFormAdmin(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'mobile_number']


class SignUpForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'first_name', 'last_name', 'mobile_number']

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user