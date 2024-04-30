from django.shortcuts import render
from django.views import generic
from .models import Recipes, Comments
# Create your views here.
class RecipeList(generic.ListView):
    queryset = Recipes.objects.all()
    template_name = "post_list.html"