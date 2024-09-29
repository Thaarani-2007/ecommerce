from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from autoslug import AutoSlugField

from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')


    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self) :
        return self.name  

    def get_absoulute_url(self):
        return f'/{self.slug}/'
    

class Product(models.Model):
    Category=models.ForeignKey(Category,related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')
    date_added=models.DateField(auto_now=True, auto_now_add=False)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    image = models.ImageField(upload_to='upload/', blank=True, null=True)
    thumbnail = models.DateTimeField(auto_now_add=True)
        

    class Meta:
        ordering = ('-date_added',)

    def __str__(self) :
        return self.name  

    def get_absoulute_url(self):
        return f'/self.category.slug/{self.slug}/'    
    
    def get_image(self):
        if self.image:
            return "http://127.0.0.1:8000/"  + self.image.url
        return ' '
    
    def get_thumbnail(self):
        if self.thumbnail:
             return "http://127.0.0.1:8000/"  + self.thumbnail.url

        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return "http://127.0.0.1:8000/"  + self.thumbnail.url
           
            else:
                return ''
    def make_thumbnail(slef,image,size=(300,200)) :
        img = image.open(image)     
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=80)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
    


class Item(models.Model):
    Category=models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    image = models.ImageField(upload_to='upload/', blank=True, null=True)
    is_sold=models.BooleanField(default=False)
    created_by=models.ForeignKey(User,related_name="items",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)  

    class Meta:
        ordering = ('-created_at',)

    def __str__(self) :
        return self.name        
    
class UserProfile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField()
    mobile_number = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
 


    