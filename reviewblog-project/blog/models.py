from django.db import models

# Create your models here.
class Blog(models.Model):
	image = models.ImageField(upload_to = 'images/')
	character = models.CharField(max_length = 300)

	def __str__(self):
		return self.character