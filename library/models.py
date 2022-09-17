from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint
# Create your models here.

class CustomUser(AbstractUser):
    pass
    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=300)
    pub_date = models.DateField()
    genre = models.CharField(max_length=250)
    featured = models.BooleanField(default=False)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['title', 'author'], name='unique_constraint')
        ]
    
    def __str__(self):
        return f'{self.title} by: {self.author}'


class Tracker(models.Model):
    READING = 'RG'
    READ = 'RD'
    UNREAD = 'UR'
    STATUS_CHOICES = [
        (READING, 'reading'),
        (READ, 'read'),
        (UNREAD, 'unread'),
    ]

    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=UNREAD)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name = 'reader')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_title')

    def __str__(self):
        return f'{self.book}'


class Comments(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name = 'comments')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book')
    created_at = models.DateField(db_index=True, auto_now_add=True, null=True)
    notes = models.TextField()
    page_number = models.PositiveIntegerField(null=True)
    privacy = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.book}, {self.created_at}'