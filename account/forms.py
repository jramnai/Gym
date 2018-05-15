from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(required=False)
    mobile = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'full_name', 'email',
                  'mobile', 'password1', 'password2',)
