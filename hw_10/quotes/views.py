from django.shortcuts import render
from django.core.paginator import Paginator

from authors.models import Author
from .models import Quote

def main_quotes(request, page=1):
    per_page = 10
    quotes = Quote.objects.all()
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})

from django.shortcuts import render, redirect
from .forms import QuoteForm

def create_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            # Тут ви можете використовувати дані з форми, як раніше
            author = form.cleaned_data['author']
            quote = form.cleaned_data['quote']
            tags = form.cleaned_data['tags'] #.split(',')

            # Збереження даних у PostgreSQL
            new_quote = Quote(author=author, quote=quote)
            new_quote.save()

            # author, created = Author.objects.get_or_create(fullname=author_fullname)

            # Додавання тегів до цитати
            new_quote.tags.add(*tags)

            return render(request, 'create_quote.html', {'author': author, 'quote': quote, 'tags': tags})
    else:
        form = QuoteForm()
    return render(request, 'create_quote.html', {'form': form})

# Create your views here.
