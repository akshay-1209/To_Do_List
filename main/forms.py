from django import forms
from django.contrib.auth.models import User

class userForms(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': ' Username'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': ' Password'}))

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': ' Password'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': ' Password Confirm'}))
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Username'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    
