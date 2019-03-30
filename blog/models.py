from django.conf import settings
from django.db import models
from django.utils import timezone

# post model: what a post will be comprised of
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

# publish function that will show published date and save the post
    def publish(self):
        self.published_date = timezone.now()
        self.save()

# showing the title of the post
    def __str__(self):
        return self.title