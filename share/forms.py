from .models import Share
from django import forms



class ShareABookForm(forms.ModelForm):
    """
    Form for Book
    """
    class Meta:
        model = Share
        fields = ('name', 'title', 'author', 'picture',)