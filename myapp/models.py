from django.db import models

# Create your models here.
class BlogModel(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(blank=True)

    def __str__(self):
        return self.title
