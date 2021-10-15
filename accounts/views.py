from .forms import UserEditForm, ProfileForm, AddressForm
from django.db import transaction
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from .models import Participant, Address


def user_is_participant(user):
    return Participant.objects.filter(user=user).exists()


@login_required
@transaction.atomic
@user_passes_test(user_is_participant)
def update_profile(request):
    if request:
        participant = Participant.objects.get(user=request.user)
        if request.method == 'POST':
            user_form = UserEditForm(request.POST, instance=request.user)
            profile_form = ProfileForm(request.POST, instance=participant)
            address_form = AddressForm(
                request.POST, instance=participant.address)
            if user_form.changed_data() and user_form.is_valid():
                user_form.save()
                messages.success(request, 'User was successfully updated!')
            else:
                messages.error(request, "Please correct errors in user")
            if profile_form.changed_data() and profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Profile was successfully updated!')
            else:
                messages.error(request, "Please correct errors in profile")
            if address_form.changed_data() and address_form.is_valid():
                address_form.save()
                number_of_users = Participant.objects.filter(
                    address=address_form.instance.pk).count()
                if number_of_users > 1:
                    address = address_form.cleaned_data
                    new_address = Address.objects.create(address['fullAddress'], address['address1'],
                                           address['address2'], address['zip_code'], address['city'], address['country'])
                    participant.address = new_address
                    participant.save()
                messages.success(
                    request, 'Your address was successfully updated!')
                return render(request, 'account/profile.html', {'user_form': user_form, 'participant_form': profile_form, 'address_form': address_form})
            else:
                messages.error(request, 'Please correct the errors in address.')
        else:
            user_form = UserEditForm(instance=request.user)
            profile_form = ProfileForm(instance=participant)
            address_form = AddressForm(instance=participant.address)
            return render(request, 'account/profile.html', {'user_form': user_form, 'participant_form': profile_form, 'address_form': address_form})
