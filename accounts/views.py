from django.views.generic.edit import UpdateView
from .models import Profile
from .forms import ProfileForm

# Create your views here.
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'account/profile_update.html'

    def get_object(self):
        return Profile.objects.get(user=self.request.user) # or request.POST