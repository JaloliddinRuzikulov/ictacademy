from django.db import models

# Create your models here.



class Mentors(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)

    github = models.CharField(max_length=200, null=True, blank=True)
    linkedin = models.CharField(max_length=200, null=True, blank=True)
    telegram = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self) -> str:
        return f"{self.name} - {self.profession}"
    



class Feedback(models.Model):
    full_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    feedback = models.TextField()
    image = models.ImageField( null=True, blank=True)
    company = models.CharField(max_length = 50, null=True, blank=True)
    company_logo = models.ImageField(upload_to='logo/', null=True, blank=True)


class Projects(models.Model):
    product_name = models.CharField(max_length=150)
    product_image = models.ImageField(upload_to='product/')
    product_image_2 = models.ImageField(upload_to='product/')
    product_url_web = models.CharField(max_length=250, null=True, blank=True)
    product_url_ios = models.CharField(max_length=250, null=True, blank=True)
    product_url_android = models.CharField(max_length=250, null=True, blank=True)


    spend_time = models.IntegerField()
    users = models.IntegerField()

    mijoz_haqida = models.TextField(null=True, blank=True)
    talablar = models.TextField(null=True, blank=True)
    topshirilgan_sana = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.product_name