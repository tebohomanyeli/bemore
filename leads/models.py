from django.db import models

# Create your models here.

class Lead(models.Model):


    #----- Drop down option for source of data
    SOURCE_CHOICES = (
        ('Facebook', 'Facebook'),
        ('Instagram','Instagram'),
        ('Twitter', 'Twitter'),
        ('LinkedIn', 'Linkedin'),
        ('YouTube', 'YouTube'),
        ('Google' , 'Google'),
        ('WhatsApp' , 'WhatsApp'),    
    )

    #--------------------------------------------------------------------------Create Columns
    #----- Basic User names
    first_name  :str    = models.CharField(max_length=40)
    last_name   :str    = models.CharField(max_length=30)
    age         :int    = models.IntegerField(default=0)
    
    called      :bool   = models.BooleanField(default=False)
    source      :str    = models.CharField(choices=SOURCE_CHOICES, max_length=100)

    profile_pricture = models.ImageField(blank=True, null=True) #Make PP optional
    special_files = models.FileField(blank=True, null=True)