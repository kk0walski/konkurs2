from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.conf import settings

# Create your views here.
class CurrentUserMixin(object):
    model = settings.AUTH_USER_MODEL

    def get_object(self, *args, **kwargs):
        try:
            obj = super(CurrentUserMixin, self).get_object(*args, **kwargs)
        except AttributeError:
            # SingleObjectMixin throws an AttributeError when no pk or slug
            # is present on the url. In those cases, we use the current user
            obj = self.request.user

        return obj

class UserDetailView(CurrentUserMixin, DetailView):
    template_name = 'account/profile.html' 