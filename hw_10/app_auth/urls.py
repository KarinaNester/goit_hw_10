from django.urls import path
from . import views

app_name = "app_auth"

urlpatterns = [
    path('signup/', views.signupuser, name='registration'),
    path('login/', views.loginuser, name='login'),
    path('auth/logout/', views.logoutuser, name='logout')

]