from django.db import models

# Create your models here.

          
          

class Signup(models.Model):
          
          Albion_username = models.CharField(max_length=30)
          servers = models.CharField(max_length=25)
          email = models.CharField(max_length=100, unique=True)
          password= models.Password()


class CocaptainModel(models.Model):
        name =  models.CharField(max_length=30)
        description = models.TextField(max_length=50)
        fame = models.IntegerField()

        def __str__(self):
                return self.name
        
class MemberModel(models.Model):
        name =  models.CharField(max_length=30)
        description = models.TextField(max_length=50)
        fame = models.IntegerField()

        def __str__(self):
                return self.name
        
