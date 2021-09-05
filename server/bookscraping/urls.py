from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookInfo.as_view()),
]
