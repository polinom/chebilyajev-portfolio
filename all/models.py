# coding=utf-8
from django.db import models
from django.contrib.flatpages.models import FlatPage


class Page(FlatPage):
	image = models.ImageField(upload_to='pages_media', blank=True)
	bukvitsa = models.ImageField(upload_to='pages_media', blank=True)


class Galerry(models.Model):
	CHOICES = (
			(1,'Galerry'),
			(2,'Illystrations'),
			(3,'Character Design'),
		)
	title = models.CharField(max_length=222,blank=True)
	description = models.TextField(max_length=1022, blank=True)
	image = models.ImageField(upload_to='images')
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)
	image_type = models.PositiveIntegerField(choices=CHOICES)


	def __unicode__(self):
		return self.title
