from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator

from .models import UserProfile


# ---------------------------------------------------- CREATE USER -----------------------------------------------------
class CreateUserForm(UserCreationForm):
    username_validator = UnicodeUsernameValidator()
    error_messages = {
        'unique': 'Username already exists!',
        'password_mismatch': 'Passwords do not match!'
    }

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Enter email...'
            })
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter username...',
        }),
        validators=[username_validator],
        error_messages=error_messages,
        help_text=None,
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter password...',
        }),
        help_text=password_validation.password_validators_help_text_html(),
        error_messages=error_messages,
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat password...',
        }),
        help_text=password_validation.password_validators_help_text_html(),
        error_messages=error_messages,
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        if commit:
            user.save()

        return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user_description', 'user_avatar', 'user_uploaded_recipes']

        widgets = {
            'user_description': forms.TextInput(attrs={
                'placeholder': 'User description...',
            }),
            'user_avatar': forms.ClearableFileInput(attrs={
            })
        }


# ----------------------------------------------------- PWD RESET ------------------------------------------------------
class UserPasswordResetForm(PasswordResetForm):
    """
    Override default PasswordRestForm to remove label and to add placeholder
    """

    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your user email...',
        })
    )


# ----------------------------------------------------- EDIT USER ------------------------------------------------------
class EditUserForm(forms.ModelForm):
    class Meta:
        model = User

        fields = ['username', 'email', 'first_name', 'last_name']


class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile

        fields = ['user_description', 'access_level']
