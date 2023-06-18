from django.db import models

# Create your models here.

class ArticleCategory(models.Model):
    category = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.category

class Article(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE)
    subtitle = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


