from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import Quote

def main_quotes(request, page=1):
    per_page = 10
    quotes = Quote.objects.all()
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})

from django.shortcuts import render
from .forms import QuoteForm

@login_required
def create_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():

            author = form.cleaned_data['author']
            quote = form.cleaned_data['quote']
            tags = form.cleaned_data['tags'] #.split(',')


            new_quote = Quote(author=author, quote=quote)
            new_quote.save()


            new_quote.tags.add(*tags)

            return render(request, 'create_quote.html', {'author': author, 'quote': quote, 'tags': tags})
    else:
        form = QuoteForm()
    return render(request, 'create_quote.html', {'form': form})


