from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Address, Participant


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', ]


admin.site.register(CustomUser, CustomUserAdmin)


class ParticipantAdmin(admin.ModelAdmin):
    model = Participant
    list_display = ("user", "nationality", "birthday")
    list_filter = ("user", "nationality", "birthday", "address")
    fieldsets = (
        (_("Contact info"), {
         "fields": ("user", "phone_number", "cellphone_number")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "birthday",
                    "site",
                    "nationality",
                    "address"
                )
            },
        ),
    )
    search_fields = ("user",)
    ordering = ("user", "nationality")


admin.site.register(Participant, ParticipantAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_filter = ("country", "city", "zip_code")
    list_display = ("fullAddress", "zip_code", "city", "country")
    fieldsets = (
        (_("Basic info"), {
         "fields": ("fullAddress", "country", "city")}),
        (
            _("Address info"),
            {
                "fields": (
                    "address1",
                    "address2",
                    "zip_code",
                )
            },
        ),
    )


admin.site.register(Address, AddressAdmin)
