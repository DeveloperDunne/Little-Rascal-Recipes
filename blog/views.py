from django.shortcuts import render
from django.views import generic
from .models import Recipe, Comment
# Create your views here.

class RecipeList(generic.ListView):
    queryset = Recipe.objects.all()
    template_name = "post_list.html"