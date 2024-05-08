from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Share
from .forms import ShareABookForm
# Create your views here.


def share_a_book(request):
    shared_list = Share.objects.all().filter(
        approved=True)

    if request.method == "POST":
        share_a_book_form = ShareABookForm(request.POST, request.FILES)
        if share_a_book_form.is_valid():
            share_a_book_form.save()
            messages.add_message(request, messages.SUCCESS, "Thanks for sharing!!")
    """
    Renders the Share page
    """
    share_a_book_form = ShareABookForm

    return render(
        request,
        "share/share.html",

        {"share_a_book_form": share_a_book_form,
         'shared':shared_list}
    )