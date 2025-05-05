from django.db import models

# Create your models here.
class Info(models.Model):

    phone = models.CharField(max_length=100)
    email = models.EmailField()
    location = models.CharField(max_length=200)


class Slider(models.Model):

    image = models.ImageField(upload_to='slider')
    text1 = models.TextField()
    text2 = models.TextField()
    text3 = models.TextField()
    text4 = models.TextField()


class Product(models.Model):

    image = models.ImageField(upload_to='product')
    price = models.PositiveIntegerField('Product price')
    name = models.CharField('Product name', max_length=100)

    def __str__(self):
        return self.name


class Brand_Product(models.Model):

    image = models.ImageField(upload_to='barnd_product')
    price = models.PositiveIntegerField('Brand_Product price')
    name = models.CharField('Brand_Product name', max_length=100)

    def __str__(self):
        return self.name
    

class Contact(models.Model):

    name = models.CharField('Contact name', max_length=60)
    email = models.EmailField('Contact email')
    phone = models.CharField('Contact phone', max_length=60)
    message = models.TextField('Contact message')

    def __str__(self):
        return self.name