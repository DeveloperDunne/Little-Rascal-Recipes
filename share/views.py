from django.shortcuts import render
from django.contrib import messages
from .models import Share
from .forms import ShareABookForm
# Create your views here.

def share_a_book(request):

    if request.method == "POST":
        share_a_book_form = ShareABookForm(data=request.POST)
        if share_a_book_form.is_valid():
            share_a_book_form.save()
            messages.add_message(request, messages.SUCCESS, "Thanks for sharing!!")
    """
    Renders the Contact page
    """
    share_a_book_form = ShareABookForm

    return render(
        request,
        "share/share.html",
        {"share_a_book_form": share_a_book_form,}
    )