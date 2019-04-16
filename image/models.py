from django.db import models
from utils.abstract_model import AbstractModel

class Image(AbstractModel):

	image = models.ImageField(blank=True)
