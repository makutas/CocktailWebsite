from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth import password_validation


class RegisterUserForm(UserCreationForm):
    username_validator = UnicodeUsernameValidator()
    error_messages = {'unique': 'Username already exists!'}

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-row',
            'placeholder': 'Enter new user\'s name...',
        }),
        validators=[username_validator],
        error_messages=error_messages,
        help_text=None,
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'user-password-row',
            'placeholder': 'Enter password...',
        }),
        help_text=password_validation.password_validators_help_text_html()
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'user-password-row',
            'placeholder': 'Repeat password...',
        }),
        help_text=password_validation.password_validators_help_text_html()
    )

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
        )

    # TODO - email required (check stuff how to change pass and forget)

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        print(user.username)
        if commit:
            user.save()

        return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user_description', 'user_avatar']

        widgets = {
            'user_description': forms.TextInput(attrs={
                'class': 'form-row',
                'placeholder': 'User description...',
            }),
            'user_avatar': forms.ClearableFileInput(attrs={
                'class': 'form-row',
            }),
        }
