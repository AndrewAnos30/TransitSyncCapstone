from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.forms import PasswordResetForm
from users.models import CustomUser
from .models import CurrentPrice, TranspoType


class ConductorRegistrationForm(UserCreationForm):

    phone_regex = RegexValidator(
        regex=r'^09\d{9}$',  # Matches "09" followed by 8 digits
        message="Phone number must be 11 digits and start with '09********'",
    )
    contactNumber = forms.CharField(validators=[phone_regex], max_length=11, required=False, widget=forms.TextInput(attrs={'placeholder': '09*********'}))
    emergencyContact = forms.CharField(validators=[phone_regex], max_length=11, required=False, widget=forms.TextInput(attrs={'placeholder': '09*********'}))
    email = forms.EmailField(help_text='A valid email address, please.', required=True)
    birthDate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'middle_name', 'last_name', 'username', 'email', 'password1', 'password2',
                        'gender', 'age', 'birthDate', 'contactNumber', 'emergencyContact', 'contactPerson',
                          'DPA','TransportationType' ]
        
        
    def save(self, commit=True):
        user = super(ConductorRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    

class CashierRegistrationForm(UserCreationForm):

    phone_regex = RegexValidator(
        regex=r'^09\d{9}$',  # Matches "09" followed by 8 digits
        message="Phone number must be 11 digits and start with '09********'",
    )
    contactNumber = forms.CharField(validators=[phone_regex], max_length=11, required=False, widget=forms.TextInput(attrs={'placeholder': '09*********'}))
    emergencyContact = forms.CharField(validators=[phone_regex], max_length=11, required=False, widget=forms.TextInput(attrs={'placeholder': '09*********'}))
    email = forms.EmailField(help_text='A valid email address, please.', required=True)
    birthDate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'middle_name', 'last_name', 'username', 'email', 'password1', 'password2',
                        'gender', 'age', 'birthDate', 'contactNumber', 'emergencyContact', 'contactPerson',
                         'DPA' ]
        
        
    def save(self, commit=True):
        user = super(CashierRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class KilometerForm(forms.Form):
    kilometers = forms.FloatField(label='Kilometers')
    car_type = forms.ChoiceField(
        label='Car Type',
        choices=TranspoType.STATUS,  # Use the choices from the TranspoType model
        widget=forms.Select(attrs={'class': 'form-control'})
    )

