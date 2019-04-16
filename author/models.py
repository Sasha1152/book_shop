from django.db import models
from utils.abstract_model import AbstractModel
from image.models import Image


class Author(AbstractModel):
	first_name = models.CharField(max_length=64, blank=True)
	last_name = models.CharField(max_length=64, blank=True)
	biography = models.TextField()
	image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
