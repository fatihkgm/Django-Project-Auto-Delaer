from django.db import models

# Create your models here.


class Teams(models.Model):
	first_name= models.CharField(max_length=255)
	last_name= models.CharField(max_length=255)
	designation= models.CharField(max_length=255)
	photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
	facebook_link = models.URLField(max_length=100)
	twitter_link = models.URLField(max_length=100)
	google_plus_link = models.URLField(max_length=100)
	created_date = models.DataTimeField(auto_now_add=True)


