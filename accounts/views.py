from django.core.checks import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic.detail import DetailView
from django.conf import settings
from .models import Participant


def user_is_participant(user):
    return Participant.objects.filter(user=user).exists()

from .forms import UserEditForm, ProfileForm, AddressForm
from django.db import transaction

@login_required
@transaction.atomic
@user_passes_test(user_is_participant)
def update_profile(request):
    if request:
        participant = Participant.objects.get(user=request.user)
        if request.method == 'POST':
            user_form = UserEditForm(request.POST, instance=request.user)
            profile_form = ProfileForm(request.POST, instance=participant)
            address_form = AddressForm(request.POST, instance=participant.address)
            if user_form.is_valid() and profile_form.is_valid() and address_form.is_valid():
                user_form.save()
                profile_form.save()
                address_form.save()
                messages.success(request, 'Your profile was successfully updated!')
                return render(request, 'account/profile.html', {'user_form': user_form, 'participant_form': profile_form, 'address_form': address_form})
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            user_form = UserEditForm(instance=request.user)
            profile_form = ProfileForm(instance=participant)
            address_form = AddressForm(instance=participant.address)
            return render(request, 'account/profile.html', {'user_form': user_form, 'participant_form': profile_form, 'address_form': address_form})
