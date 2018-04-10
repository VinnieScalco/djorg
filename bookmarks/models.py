from django.db import models

class bookmarks(models.Model):
	name = models.CharField(max_length = 1000)
	url = models.URLField()