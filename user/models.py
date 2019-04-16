from django.db import models
from utils.abstract_model import AbstractModel
from image.models import Image

class User(AbstractModel):
	first_name = models.CharField(max_length=64, blank=True)
	last_name = models.CharField(max_length=64, blank=True)
	email = models.EmailField()
	password = models.CharField(max_length=32)
	phone_number = models.CharField(blank=True, max_length=16)
	wallet = models.DecimalField(max_digits=6, decimal_places=2)
	image = models.ForeignKey(Image, on_delete=models.CASCADE)

	def __str__(self):
		return self.email