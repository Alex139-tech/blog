from django.contrib import admin
from .models import Post, Comment, Reply

class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'caption', 'created_at', 'image']  # Use 'caption' instead of 'title'
    search_fields = ['caption']  # Search functionality for 'caption'

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'user', 'created_at']
    search_fields = ['content']

class ReplyAdmin(admin.ModelAdmin):
    list_display = ['comment', 'user', 'created_at']
    search_fields = ['content']

# Register the models with custom admins
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reply, ReplyAdmin)
