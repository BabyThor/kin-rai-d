from __future__ import unicode_literals

from django.db import models

class Tag(models.Model):
	tag_type_choices = (
		('style', 'Style'),
		('location', 'Location')
	)
	name = models.CharField(max_length=200)
	tag_type = models.CharField(max_length=200, choices=tag_type_choices)

	def __unicode__(self):
		return '%s : %s' % (self.name, self.tag_type)

class Restaurant(models.Model):
	name = models.CharField(max_length=200)
	tags = models.ManyToManyField('food.Tag')
	latitude = models.FloatField(null=True, blank=True)
	longitude = models.FloatField(null=True, blank=True)

	def __unicode__(self):
		return self.name

class Menu(models.Model):
	name = models.CharField(max_length=200)
	restaurant = models.ForeignKey('food.Restaurant')
	price = models.IntegerField()

	def __unicode__(self):
		return self.name


