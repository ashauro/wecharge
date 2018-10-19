from django.db import models
from django.contrib.auth.models import User
from chargemap.models import Country, City
from PIL import Image

# Create your models here.

class Car (models.Model):
   name = models.CharField(max_length=100, null=True)
   plate = models.CharField(max_length=9, null=True)
   acc = models.FloatField(max_length=5, null=True)
   def __str__(self):
       return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_image = models.ImageField(default='default.png', upload_to='users/profile_pics')
    user_country = models.ForeignKey(Country, null=True, on_delete=models.CASCADE)
    user_city = models.ForeignKey(City, null=True, on_delete=models.CASCADE)
    user_car = models.ForeignKey(Car, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
    def save(self, **kwargs):
        super().save()

        img = Image.open(self.user_image.path)

        if img.height > 300 or img.width > 300:
             output_size =  (300, 300)
             img.thumbnail(output_size)
             img.save(self.user_image.path)

