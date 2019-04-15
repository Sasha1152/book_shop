from django.db import models

class Book(models.Model):

	author = models.CharField(max_length=50)
	title = models.CharField(max_length=50)
	year = models.IntegerField(max_length=4)
	pages = models.IntegerField(max_length=4)
	description = models.CharField(blank=True, max_length=250)
	image = models.ImageField(blank=True)


	def __str__(self):
		return self.title
