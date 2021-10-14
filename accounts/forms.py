from django.forms.widgets import Widget
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
import datetime
from .models import ISO_3166_CODES
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Participant, Address


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
    birthday = forms.DateField(input_formats=['%Y-%m-%d'],
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
    full_address = forms.CharField(max_length=1024)
    street_address1 = forms.CharField(
        help_text="Street address, P.O. box, company, name, c/o", max_length=1024)
    street_address2 = forms.CharField(
        help_text="Appartment, suite, unit building, floor, etc.", max_length=1024)
    postal_code = forms.CharField(max_length=12)
    city = forms.CharField(max_length=1024)
    country = forms.ChoiceField(choices=ISO_3166_CODES)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        participant = Participant(user=user)
        participant.site = self.cleaned_data['site']
        participant.birthday = self.cleaned_data['birthday']
        participant.place_of_birth = self.cleaned_data['place_of_birth']
        participant.phone_number = self.cleaned_data['phone_number']
        participant.cellphone_number = self.cleaned_data['cellphone_number']
        participant.nationality = self.cleaned_data['nationality']
        participant.save()
        address = Address(user=user)
        address.fullAddress = self.cleaned_data['full_address']
        address.address1 = self.cleaned_data['street_address1']
        address.address2 = self.cleaned_data['street_address2']
        address.zip_code = self.cleaned_data['postal_code']
        address.city = self.cleaned_data['postal_code']
        address.country = self.cleaned_data['country']
        address.save()
        return user
