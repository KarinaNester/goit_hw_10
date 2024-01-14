from django import forms

from authors.models import Author
from quotes.models import Quote


# class QuoteForm(forms.Form):
#     author = forms.CharField(max_length=100)
#     quote = forms.CharField(widget=forms.Textarea)
#     tags = forms.CharField(max_length=200, help_text='Enter tags separated by commas')


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['author', 'quote', 'tags']
        # widgets = {
        #     'author': forms.Select(attrs={'class': 'form-control'}),  # Додаємо клас для стилізації
        #     'quote': forms.Textarea(attrs={'class': 'form-control'}),
        #     'tags': forms.TextInput(attrs={'class': 'form-control'}),
        # }