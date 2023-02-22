from django.db import models

# Create your models here.

class Otp(models.Model):
    otp= models.IntegerField()
    mobile= models.TextField(max_length=13)
    created_at= models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.mobile+'-'+str(self.otp)
    
class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')    
    uniqueId= models.TextField(max_length=50)
    