from typing import Any
from django.contrib.auth.models import BaseUserManager

class CustomManager(BaseUserManager):
          def create_user(self,Email,Password = None, **extra_fields):
                  if not Email:
                              raise ValueError('Email FIeld required')
                  if not Password:
                              raise ValueError("The Password field is required")
                  
                  Email = self.normalize_email(Email)
                  user = self.model(Email=Email,**extra_fields)
                  user.set_password(Password)
                  user.save(using=self._db)
                  return user
                  


          def create_superuser(self, Email, Password=None, **extra_fields):
                    extra_fields.setdefault("is_staff", True)
                    extra_fields.setdefault("is_superuser", True)
                    extra_fields.setdefault("is_member", True)

                    if extra_fields.get("is_staff") is not True:
                              raise ValueError("Superuser must have is_staff=True.")
                    if extra_fields.get("is_superuser") is not True:
                              raise ValueError("Superuser must have is_superuser=True.")
        
                    return self.create_user(Email, Password, **extra_fields)
         