from rest_framework import serializers
from .models import Book, Tracker, Comments




class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', 'author', 'pub_date',
                'genre', 'featured', )


class TrackerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tracker
        fields = ('status', 'user', 'book', )


class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
            model = Comments
            fields = ('user', 'book', 'created_at', 'notes', 'page_number', 'privacy')