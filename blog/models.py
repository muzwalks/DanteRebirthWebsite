from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	date = models.DateTimeField()
	signature = models.CharField(max_length=140, default = "This too shall pass")

	def __str__(self):
		return self.title

# Create your models here.
