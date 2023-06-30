from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.



#----- Get build in user model
class User(AbstractUser):
    pass



class Lead(models.Model):

    #--------------------------------------------------------------------------Create Columns
    #----- Basic User names
    first_name  :str    = models.CharField(max_length=40)
    last_name   :str    = models.CharField(max_length=30)
    age         :int    = models.IntegerField(default=0)

    #----- link an agent to each lead created
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)


    #----- add a default viewing option when print the Agent class
    def __str__(self):
        return f"{self.first_name} {self.last_name}"




class Agent(models.Model):

    #----- decide what happens to an agent when a lead is deleted.
    user = models.OneToOneField("User", on_delete=models.CASCADE)


    #----- add a default viewing option when print the Agent class
    def __str__(self):
        return self.user.email






