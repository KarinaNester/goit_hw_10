from .models import Author
from django.shortcuts import render, redirect, get_list_or_404
from .forms import AuthorForm


def authors(request, fullname):
    try:
        author = Author.objects.get(fullname=fullname)
        author_info = {
            "fullname": author.fullname,
            "born_date": author.born_date,
            "born_location": author.born_location,
            "description": author.description
        }
        return render(request, 'author_detail.html', {'author_info': author_info})
    except Author.DoesNotExist:
        return render(request, 'author_not_found.html')

# authors/views.py

from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Author


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    file_path = author.fullname  # припустимо, що це шлях до файлу

    # Передати дані у шаблон і відображення
    return render(request, 'authors/author_detail.html', {'file_path': file_path, 'author': author})


def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            # Збереження даних у базі даних
            form.save()

            # Отримання ім'я шляху або шляху за допомогою reverse
            author = form.save()  # Зберегти об'єкт автора в базу даних
            url = reverse('authors:author_detail', args=[author.id])

            # Редирект на відповідний шлях
            return redirect(url)
    else:
        form = AuthorForm()
    return render(request, 'authors/create_author.html', {'form': form})

# Create your views here.
