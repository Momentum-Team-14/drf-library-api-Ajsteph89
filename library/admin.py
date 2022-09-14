from django.contrib import admin
from .models import CustomUser, Book, Tracker, Comments
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Book)
admin.site.register(Tracker)
admin.site.register(Comments)
