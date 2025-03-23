from django.db import models
from django.contrib.auth.models import User

# post models
class Post(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photo/', blank=True, null=True)  # ✅ Image field
    caption = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)  # Correctly defined
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"posts by {self.user.username} - {self.caption[:20]}"

    

# Comment Model
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"comment by {self.user.username} - {self.text[:20]}"

# Reply Model
class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} replied - {self.text[:20]}"
