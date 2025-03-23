from django.contrib import admin
from .models import Post, Comment, Reply  # Apne models import karein

# Basic Registration
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reply)
