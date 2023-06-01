from django.db import models

# Create your models here.
class CourseCategory(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.category
    

class Courses(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)

    image = models.ImageField(null=True, blank=True)

    course_length = models.IntegerField(null=True, blank=True)
    course_length_desc = models.CharField(max_length=150, null=True, blank=True)
    modules = models.IntegerField(null=True, blank=True)
    modules_desc = models.CharField(max_length=150, null=True, blank=True)
    lessons = models.IntegerField(null=True, blank=True)
    lessons_desc = models.CharField(max_length=150, null=True, blank=True)
    

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.full_name} - {self.phone}"

