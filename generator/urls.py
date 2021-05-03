from django.urls import path
from generator import views
urlpatterns=[path('hello/', views.hello, name='password'),]