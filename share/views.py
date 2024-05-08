from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Share
from .forms import ShareABookForm
# Create your views here.

class SharedList(generic.ListView):
    queryset = Share.objects.filter(approved=True)
    template_name = "share/share.html"
    paginate_by = 6

def share_a_book(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """
    
    share = get_object_or_404(slug=slug)
    shared_list = share.all().order_by("-created_on")(approved=True)
    
    if request.method == "POST":
        share_a_book_form = ShareABookForm(data=request.POST)
        if share_a_book_form.is_valid():
            shared = share_a_book_form.save(commit=False)
            shared.share = request.user
            shared.share = shared
            share.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Book submitted and awaiting approval'
            )
    
    share_a_book_form = ShareABookForm()

    return render(
        request,
        "share/share.html",
        {
            "share": shared,
            "shared_list": shared_list,
            "share_a_book_form": share_a_book_form
        },
    )
