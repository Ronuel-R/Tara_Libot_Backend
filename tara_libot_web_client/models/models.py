from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from tara_libot_web_client.storage import OverwriteStorage
from mapbox_location_field.models import LocationField

def rename_profile(instance, filename):
    extension = filename.split('.')[-1]
    og_filename = filename.split('.')[0]
    new_filename = "%s_profile.%s" % (instance.user.username, extension)
    return new_filename
def upload_profile_location(instance, filename):
    
    new_file = rename_profile(instance,filename)
    return 'Profiles/%s/%s' % (instance.user.username, new_file)
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(blank = True,upload_to=upload_profile_location,storage=OverwriteStorage())
    age = models.IntegerField(null = True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    date_of_birth = models.DateField(null = True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_num = models.CharField(max_length=15)
    created = models.DateTimeField(default=timezone.now, null=False,editable=False)
    modified = models.DateTimeField()



    class Meta:
        verbose_name = 'Account'
        
    def __str__(self):
        return self.user.first_name

class Business(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    created_at = models.DateField()
    modified_at = models.DateField()
    business_photo = models.ImageField(null=True)
    closing_time = models.DateTimeField()
    opening_time = models.DateTimeField()
    rating = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    location= LocationField()
    
    def __str__(self):
        return self.name

class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length= 2000)
    business = models.ForeignKey(Business,on_delete=models.CASCADE)
    rating = models.FloatField()
    created_by= models.ForeignKey(Account, on_delete=models.CASCADE )
    created_at = models.DateField(timezone.now,null=False,editable=False)
    likes= models.IntegerField()
    #reply_comment=models.ForeignKey(Comments, on_delete= models.CASCADE )
    def __str__(self):
        return self.content

class Foods(models.Model):
    BREAKFAST = 'Umagahan'
    EATERY = 'Karinderya'
    CARINDERIA = 'Turo-Turo'
    LUNCH = 'Tanghalian'
    PASALUBONG = 'Pasalubong'

    CATEGORY_CHOICES = [
        (BREAKFAST, 'Umagahan'),
        (EATERY, 'Karinderya'),
        (CARINDERIA, 'Turo-Turo'),
        (LUNCH, 'Tanghalian'),
        (PASALUBONG, 'Pasalubong'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    price = models.FloatField()
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    food_photo = models.ImageField(null=True)

class FoodComments(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length= 2000)
    food = models.ForeignKey(Foods,on_delete=models.CASCADE)
    rating = models.FloatField()
    created_by= models.ForeignKey(Account, on_delete=models.CASCADE )
    created_at = models.DateField(timezone.now,null=False,editable=False)
    likes= models.IntegerField()
    #reply_comment=models.ForeignKey(Comments, on_delete= models.CASCADE )
    def __str__(self):
        return self.content
    
    