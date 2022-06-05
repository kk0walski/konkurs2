from django.views.generic import TemplateView
from django.shortcuts import redirect

class AboutPageView(TemplateView):
    template_name = "pages/about.html"

class ProfilePageView(TemplateView):
    template_name = "pages/profile.html"

class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('account_login')
        return super(HomePageView, self).dispatch(request, *args, **kwargs)

