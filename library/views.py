from django.shortcuts import render
from rest_framework import generics, mixins
from .models import Book, Tracker, Comments
from .serializers import BookSerializer, TrackerSerializer, CommentsSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.



class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class FeatureBook(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get_queryset(self):
        queryset = Book.objects.filter(featured=True)
        return queryset


class TrackerList (generics.ListCreateAPIView):
    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer

    def perform_create(self, serializer): 
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Tracker.objects.filter(user=self.request.user)
        return queryset

class TrackerDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer


class CommentsAll (generics.ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

    def get_queryset(self):
        queryset = Comments.objects.filter(privacy=False)
        return queryset

class CommentsList (generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

    def perform_create(self, serializer): 
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Comments.objects.filter(user=self.request.user)
        return queryset


class CommentsDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def api_root(request, format=None):
    return Response({
        'library': reverse('library-list', request=request, format=format),
        'tracker': reverse('tracker-list', request=request, format=format),
        'comments': reverse('comments-list', request=request, format=format),
    })
