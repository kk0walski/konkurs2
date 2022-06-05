from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Profile

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'birthday', 'place_of_birth', 'phone_number', 'cellphone_number',
                  'nationality', 'biography', 'country', 'city', 'street_line', 'site', 'zipcode')
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }