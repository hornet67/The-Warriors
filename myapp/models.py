from django.db import models

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from myapp.manager import CustomManager
from django.utils import timezone

# Create your models here.

          

class CustomUser(AbstractBaseUser,PermissionsMixin):
        GuildMemberType = [
                ('Founder', 'Founder'),
                ('CoCaptain', 'CoCaptain'),
                ('Member', 'Member'),
                ('Recuit', 'Recuit'),
        ]
        GUILD_MEMBER_CHOICES = [
                ('yes', 'Yes'),
                ('no', 'No'),
        ]
        SERVER_CHOICES = [
                ('Asia', 'Asia'),
                ('Europe', 'Europe'),
                ('N.America', 'N.America'),
        ]

        AlbionUsername = models.CharField(max_length=30) 
        Email = models.CharField(max_length=150,unique=True)
        Total_fame = models.CharField(max_length=50)  
        Kill_fame = models.CharField(max_length=50)
        Playerkill = models.IntegerField(default=0)
        Server = models.CharField(max_length=12, choices=SERVER_CHOICES, default='Asia')
        GuildMember = models.CharField(max_length=5,choices=GUILD_MEMBER_CHOICES,default='no')
        Guildmemebertype = models.CharField(max_length=10, choices=GuildMemberType, default='Recuit')
        image = models.ImageField(upload_to='Profile/',blank=True, null=True)


        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(default=False)
        is_member = models.BooleanField(default=False)
        is_superuser = models.BooleanField(default=False)
        date_joined = models.DateTimeField(default=timezone.now)

        objects = CustomManager()

        USERNAME_FIELD = 'Email'
        REQUIRED_FIELDS = ['AlbionUsername']


        def __str__(self):
                return self.AlbionUsername


































'''
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
                return self.name'''
        
