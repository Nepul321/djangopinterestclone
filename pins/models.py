from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class PinView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-datetime' , ]

class ImagePin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/posts/images/%Y/%m/%d/%H/%M")
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    is_private = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="video_post_likes", blank=True)
    dislikes = models.ManyToManyField(User, related_name="video_posts_dislikes", blank=True)
    views = models.ManyToManyField(PinView, related_name="video_post_views", blank=True)
    view_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['-datetime', ]

    def set_view_count(self):
        views = self.views.count()
        self.view_count = views
        self.save()