from django.db import models

# Create your models here.
class post(models.Model):

	POST_CHOICES = [
    ('entertainment','ENTERTAINMENT'),
    ('sports', 'SPORTS'),
    ('travel','TRAVEL'),
    ('personal_life','PERSONAL_LIFE'),
    ('health','HEALTH'),
]


	title=models.CharField(max_length=100,null=True)
	body=models.TextField(max_length=5000,null=True)
	image=models.ImageField(upload_to='post/images',null=True)
	category = models.CharField(max_length=100, choices=POST_CHOICES,default='entertainment')
	date = models.DateTimeField(auto_now_add=True, blank=True)
	user= models.CharField(max_length=100,null=True)


class like(models.Model):
	title=models.CharField(max_length=100,null=True)
	user= models.CharField(max_length=100,null=True)


class comment(models.Model):
	title=models.CharField(max_length=100,null=True)
	comments=models.TextField(max_length=1000,null=True)
	user= models.CharField(max_length=100,null=True)