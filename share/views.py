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
            shared_book = share_a_book_form.save(commit=False)
            shared_book.name = request.user.username
            shared_book.save()
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

def share_edit(request, slug, share_id):
    
    shared_list = Share.objects.all().filter(
        approved=True)

    if request.method == "POST":
        share_a_book_form = ShareABookForm(request.POST, request.FILES)
        if share_a_book_form.is_valid():
            share_a_book_form.save()
            messages.add_message(request, messages.SUCCESS, "Thanks for sharing!!")
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating recipe!')

    return HttpResponseRedirect(reverse('share', args=[slug]))

def share_delete(request, slug, share_id):
    """
    Delete a shared post
    """
    queryset = Share.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    share = get_object_or_404(Share, pk=share_id)

    if share.name == request.user:
        share.delete()
        messages.add_message(request, messages.SUCCESS, 'Cookbook deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own shared cookbooks!')

    return HttpResponseRedirect(reverse('share', args=[slug]))