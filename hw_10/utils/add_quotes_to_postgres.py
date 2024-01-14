import os
import django
import json
import sys
sys.path.append('/Users/user/Documents/hw_10/hw_10')

from django.utils import timezone



# Встановлення змінної середовища DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw_10.settings')
django.setup()
from authors.models import Author
from quotes.models import Quote, Tag
from django.db.utils import IntegrityError

def load_quotes_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        quotes_data = json.load(file)

    for quote_data in quotes_data:
        # Перевірка, чи об'єкт із таким же текстом цитати вже існує в базі
        if not Quote.objects.filter(quote=quote_data.get('quote', '')):
            # Знаходження автора за ім'ям
            author = Author.objects.filter(fullname=quote_data.get('author', '')).first()

            # Створення об'єкта цитати
            quote = Quote.objects.create(
                quote=quote_data.get('quote', ''),
                author=author,
                created_at=timezone.now()
            )


            print(f"Цитату '{quote.quote}' успішно створено")
        else:
            print(f"Цитату '{quote_data.get('quote', '')}' вже є в базі даних")

# Вкажіть шлях до вашого JSON-файлу для цитат
quotes_file_path = 'quotes.json'

# Запустіть функцію зі шляхом до вашого JSON-файлу для цитат
load_quotes_from_json(quotes_file_path)
