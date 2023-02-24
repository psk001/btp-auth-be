from django.db import models

# Create your models here.

class Otp(models.Model):
    otp= models.IntegerField()
    mobile= models.TextField(max_length=13)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mobile+'-'+str(self.otp)
    

class Election(models.Model):
    ELECTION_TYPE_CHOICES= [
        ('NATL', 'National Election'),
        ('STAT', 'State Election'),
        ('LOCL', 'Local Election')
    ]
    type= models.TextField(max_length=4, choices=ELECTION_TYPE_CHOICES)
    name= models.TextField(max_length=100)
    id= models.UUIDField(primary_key=True)
    startDate= models.DateField()
    endDate= models.DateField()

    def __str__(self):
        return self.elction_name


class ElectionCandidate(models.Model):
    election= models.ForeignKey(Election, on_delete=models.CASCADE)
    name= models.TextField(max_length=100)
    id= models.UUIDField(primary_key=True)
    # image= models.ImageField()
    phone= models.IntegerField()
    education= models.TextField()
    dateOfBirth= models.DateField()
    description= models.TextField()

    def __str__(self):
        return self.name+'-'+self.election


class Voter(models.Model):
    name= models.TextField(max_length=100)
    id= models.UUIDField(primary_key=True)
    image= models.ImageField()
    phone= models.IntegerField()
    education= models.TextField()
    dateOfBirth= models.DateField()

    def __str__(self):
        return self.name+'-'+self.id

class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')    
    uniqueId= models.TextField(max_length=50)

    def __str__(self):
        return self.title+'-'+self.uniqueId
    