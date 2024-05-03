from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe, Comment
from .forms import CommentForm
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
    comment = recipe.comments.all().order_by("-created_on")
    comment_count = recipe.comments.filter(approved=True).count()
    comment_form = CommentForm()

    return render(
    request,
    "blog/recipe_detail.html",
    {
        "recipe": Recipe,
        "comments": comment,
        "comment_count": comment_count,
        "comment_form": comment_form,
    },
)