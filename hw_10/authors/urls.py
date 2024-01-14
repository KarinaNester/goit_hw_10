from django.urls import path
from . import views

app_name = "authors"

urlpatterns = [
    # path('authors/<str:fullname>/', views.authors, name='authors_info'),
    path('create_author/', views.create_author, name='create_author'),
    path("<int:author_id>/", views.author_detail, name="author_detail"),
    ]