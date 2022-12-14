from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from library import views


urlpatterns = [
    path('', views.api_root),
    path('library/', views.BookList.as_view(), name='library-list'),
    path('library/featured/', views.FeatureBook.as_view(), name='featured_book'),
    path('library/<int:pk>/', views.BookDetail.as_view(), name='library-detail'),
    path('tracker/', views.TrackerList.as_view(), name='tracker-list'),
    path('tracker/<int:pk>/', views.TrackerDetail.as_view(), name='tracker-detail'),
    path('comments/', views.CommentsList.as_view(), name='comments-list'),
    path('comments/<int:pk>/', views.CommentsDetail.as_view(), name='comments-detail'),
    path('comments/all/', views.CommentsAll.as_view(), name="all_comments_list")

]

urlpatterns = format_suffix_patterns(urlpatterns)