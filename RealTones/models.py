from django.db import models


# Create your models here.
class PersonalInfo(models.Model):
    city = models.TextField(blank=True, null=True)
    phone_number1 = models.IntegerField(blank=True, null=True)
    logo = models.ImageField(upload_to='images')


class slider(models.Model):
    pic = models.ImageField(upload_to='images/slides')
    text1 = models.TextField(blank=True, null=True)
    text2 = models.TextField(blank=True, null=True)


class brands_slider(models.Model):
    product_img = models.ImageField(upload_to='images/Product/Amphenol')
    product_name = models.TextField(blank=True, null=True)