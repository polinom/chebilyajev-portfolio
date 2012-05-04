from django.db import models


class About(models.Model):
	title = models.CharField(max_length=255)
	image = models.ImageField(upload_to='pages_media')
	column_one = models.TextFIeld(max_length=1024)
	column_two = models.TextFIeld(max_length=1024)


class ContactLink(models.Model):
	title = models.CharField(max_length=255)
	link = models.CharField(max_length=255)
	icon = models.ImageField(upload_to='pages_media')


class Contacts(models.Model):
	image = models.ImageField(upload_to='pages_media')
	title = models.CharField(max_length=255)
	email = models.EmailField()
	links = models.ForeignKey(ContactLink)


class HomePage(models.Model):
	image = models.ImageField(upload_to='pages_media')
	name = models.ImageField(upload_to='pages_media')


class Galerry(models.Model):
	CHOICES = (
			(1,'Galerry'),
			(2,'Illystrations'),
			(3,'Character Design'),
		)
	title = models.CharField(max_length=222)
	description = models.TextField(max_length=1022)
	image = models.ImageField(upload_to='images')
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)
	image_type = models.PositiveIntegerField(choices=CHOICES)


	def __unicode__(self):
		return self.title
