from django.db import models
from menan.models import Category

# Create your models here.
class Blogs(models.Model):
    image = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=255)
    desc = models.TextField()
    author = models.CharField(max_length=100, default='Admin')
    created_at = models.DateField(auto_now_add=True)
    comments_count = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title