from .models import Comment
from django import forms
from .forms import CommentForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)