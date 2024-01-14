from django.urls import path
from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main_quotes, name="main_quotes"),  # Обробка кореневої сторінки
    path("<int:page>", views.main_quotes, name="root_paginate"),  # Обробка сторінки з номером
    path('create_quote/', views.create_quote, name='create_quote'), # Обробка створення цитати
]




