# coding=utf-8
from django.db import models
from django.contrib.flatpages.models import FlatPage
from django.conf import settings


class Page(FlatPage):
    image = models.ImageField(upload_to='pages_media', blank=True)
    bukvitsa = models.ImageField(upload_to='pages_media', blank=True)

    @property
    def get_image(self):
        print image.url
        return image.url


class Image(models.Model):
	CHOICES = (
			('illystration','Illystration'),
			('storyboard','Storyboard'),
			('character_design','Character Design'),
		)
	title = models.CharField(max_length=222,blank=True)
	description = models.TextField(max_length=1022, blank=True)
	image = models.ImageField(upload_to='images')
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)
	gallery = models.CharField(max_length=50, choices=CHOICES)


	def __unicode__(self):
		return self.title


	def picture(self):
		return '<img src="%s" height=100>'%self.image.url

	picture.allow_tags = True
