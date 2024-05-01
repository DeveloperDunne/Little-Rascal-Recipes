from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe, Comment
# Create your views here.

class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

def recipe_detail(request, slug):
   
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/recipe_detail.html",
        {"recipe": recipe},
    )