from django.shortcuts import render
from rest_framework import generics
from .models import Book, Tracker, Comments
from .serializers import BookSerializer, TrackerSerializer, CommentsSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
# Create your views here.



class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class TrackerList (generics.ListCreateAPIView):
    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer): 
        serializer.save(owner=self.request.user)

class TrackerDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CommentsList (generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer): 
        serializer.save(owner=self.request.user)

class CommentsDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

@api_view(['GET'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def api_root(request, format=None):
    return Response({
        'library': reverse('library-list', request=request, format=format),
        'tracker': reverse('tracker-list', request=request, format=format),
        'comments': reverse('comments-list', request=request, format=format),
    })
