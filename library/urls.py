from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from library import views


urlpatterns = [
    path('library/', views.BookList.as_view()),
    path('library/<int:pk>/', views.BookDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)