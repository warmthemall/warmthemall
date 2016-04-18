from django import forms
from registration.forms import RegistrationFormUniqueEmail, RegistrationForm
from django.contrib.auth.models import User

class UserProfileRegistrationForm(RegistrationFormUniqueEmail):
    state = forms.CharField()

class UserProfileUpdateForm(RegistrationForm):
    state = forms.CharField()
    class Meta:
        model = User
        fields = ('email', 'first_name',)