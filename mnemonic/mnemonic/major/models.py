from django.db import models

# Create your models here.

class Words(Model):
	word = models.CharField(max_length=128)
