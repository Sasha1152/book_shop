from django.db import models
from utils.abstract_model import AbstractModel


class Genre(AbstractModel):
	name = models.CharField(max_length=64, blank=True)
