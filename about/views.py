from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import ContactUsForm
# Create your views here.

def about_me(request):

    if request.method == "POST":
        contact_us_form = ContactUsForm(data=request.POST)
        if contact_us_form.is_valid():
            contact_us_form.save()
            messages.add_message(request, messages.SUCCESS, "Thanks for your message! I will try to read and respond within 5 working days.")
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