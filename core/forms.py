from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from core.models import User
# from django.contrib.auth.models import User

# class LoginForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': 'Your username',
#         'class': 'w-full py-4 px-6 rounded-xl',
#     }))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={
#         'placeholder': 'Your password',
#         'class': 'w-full py-4 px-6 rounded-xl',
#     }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))

# from django.forms.widgets import ClearableFileInput

# class CustomClearableFileInput(ClearableFileInput):
#     template_name = 'core/custom_button_avatar.html'

class ChangeAvatarForm(forms.ModelForm):
    # avatar = forms.ImageField(widget=CustomClearableFileInput())
    class Meta:
        model = User
        fields = ['avatar']


class LoginFormWithEmailVerification(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    def confirm_login_allowed(self, user):
        if not user.email_verified:
            raise forms.ValidationError(
                "Email is not verified. Please check your email and verify your account."
            )