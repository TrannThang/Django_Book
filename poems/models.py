from django.db import models
from django.urls import reverse


# Create your models here.
class Poem(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    excerpt = models.TextField(null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="", null=True, blank=True)

    def get_absolute_url(self):
        return reverse("poem_detail", kwargs={"id": self.id})

    def __str__(self):
        return self.title
