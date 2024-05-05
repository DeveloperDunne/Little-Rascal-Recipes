from django.shortcuts import render
from .models import About
from .forms import ContactUsForm
# Create your views here.

def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()
    contact_us_form = ContactUsForm

    return render(
        request,
        "about/about.html",
        {"about": about,
         "contact_us_form": contact_us_form},
    )