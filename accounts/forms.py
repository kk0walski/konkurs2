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

    def get_address(self, fullAddress, address1, address2, zip, city, country):
        existing_address = Address.objects.filter(fullAddress=fullAddress, address1=address1,
                                                  address2=address2, zip_code=zip, city=city,
                                                  country=country)
        if existing_address.exists():
            return existing_address[0]
        else:
            address = Address()
            address.fullAddress = fullAddress
            address.address1 = address1
            address.address2 = address2
            address.zip_code = zip
            address.city = city
            address.country = country
            address.save()
            return address

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
        participant.address = self.existing_address(self.cleaned_data['full_address'], self.cleaned_data['street_address1'], self.cleaned_data[
            'street_address2'], self.cleaned_data['postal_code'], self.cleaned_data['postal_code'], self.cleaned_data['country'])
        participant.save()
        return user


class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ('birthday', 'place_of_birth', 'phone_number',
                  'cellphone_number', 'nationality')
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = {'fullAddress', 'address1',
                  'address2', 'zip_code', 'city', 'country'}

    def equal(self, other):
        if (self.instance.fullAddress == other.fullAddress and self.instance.address1 == other.address1 and
            self.instance.address2 == other.address2 and self.instance.city == other.city and
            self.instance.country == other.country):
            return True
        else:
            return False

    def save(self):
        data = self.cleaned_data
        number_of_users = Participant.objects.filter(
            address=self.instance).count()
        if number_of_users == 1:
            self.instance.save()
        else:
            new_address = Address(fullAddress=data['fullAddress'], address1=data['address1'],
                                         address2=data['address2'], zip_code=data['zip_code'], city=data['city'], country=data['country'])
            if new_address != self.instance:
                new_address.save()
