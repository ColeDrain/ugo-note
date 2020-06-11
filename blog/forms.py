from django import forms
from . models import Comment

class ContactForm(forms.Form):
    """ContactForm definition."""
    name = forms.CharField( max_length=50, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    """Form definition for Comment."""

    class Meta:
        """Meta definition for Commentform."""

        model = Comment
        fields = ('author', 'body')
        widgets = {
            'body': forms.Textarea(attrs={'rows':4})
        }
