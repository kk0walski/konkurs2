from django.forms.widgets import Widget
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
import datetime
from .models import ISO_3166_CODES
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Participant


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username',)


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    site = forms.URLField(required=False)
    birthday = forms.DateField(input_formats=("%d-%m-%Y"),
                               widget=forms.DateInput(attrs={"firstDay": 1,
                                                             "pattern=": "\d{4}-\d{2}-\d{2}",
                                                             "lang": "pl",
                                                             "format": "yyyy-mm-dd",
                                                             "type": "date",
                                                             }), initial=datetime.date.today)
    place_of_birth = forms.CharField(initial="Kalisz", max_length=100)
    phone_number = PhoneNumberField(required=False, widget=PhoneNumberPrefixWidget(
        initial="PL", attrs={'class': 'form-control'}))
    cellphone_number = PhoneNumberField(required=False, widget=PhoneNumberPrefixWidget(
        initial="PL", attrs={'class': 'form-control'}))
    nationality = forms.ChoiceField(required=False, choices=ISO_3166_CODES)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
