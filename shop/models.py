from django.db import models

# Create your models here.


class Product(models.Model):
    product_Id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50, default='')
    category = models.CharField(max_length=50, default='')
    subcategory = models.CharField(max_length=50, default='')
    price = models.FloatField(default=0)
    desc = models.CharField(max_length=250)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default='')

    def __str__(self):
        return self.product_name



class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    phone = models.IntegerField(default=0000000000)
    subject = models.CharField(max_length=100, default='')
    message = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.name
