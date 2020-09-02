from django.db import models

# Create your models here.

class toDoListItem(models.Model):
	content = models.TextField()
