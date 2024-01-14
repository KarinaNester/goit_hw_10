import json
import os
import django
from django.utils import timezone


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw_10.settings')
django.setup()

from authors.models import Author


def load_authors_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        authors_data = json.load(file)

    for author_data in authors_data:
        # Перевірка, чи об'єкт автора з таким fullname не існує вже у базі
        if not Author.objects.filter(fullname=author_data.get('fullname', '')):
            # Створення об'єкта автора
            author = Author.objects.create(
                fullname=author_data.get('fullname', ''),
                born_date=author_data.get('born_date', ''),
                born_location=author_data.get('born_location', ''),
                description=author_data.get('description', ''),
                created_at=timezone.now()
            )

            print(f"Author {author.fullname} successfully created")
        else:
            print(f"Author {author_data.get('fullname', '')} already exists in the database")

# Визначте шлях до вашого файлу JSON
authors_file_path = 'authors.json'


# Запускаємо функцію зі шляхом до вашого файлу JSON для авторів і цитат
load_authors_from_json(authors_file_path)
# Додайте аналогічний виклик для цитат, якщо потрібно



