from django.db import models
from image.models import Image

class User(models.Model):
	first_name = models.CharField(max_length=64, blank=True)
	last_name = models.CharField(max_length=64, blank=True)
	email = models.EmailField()
	password = models.CharField(max_length=32)
	phone_number = models.CharField(blank=True, max_length=16)
	wallet = models.DecimalField(max_digits=6, decimal_places=2, default=0)
	image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.email