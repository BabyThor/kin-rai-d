from __future__ import unicode_literals

from django.db import models

class Type(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

class Style(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

class Location(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

class Restaurant(models.Model):
	name = models.CharField(max_length=200)
	food_type = models.ForeignKey(Type)
	food_style = models.ForeignKey(Style)
	location = models.ForeignKey(Location)

	def __unicode__(self):
		return self.name

class Menu(models.Model):
	name = models.CharField(max_length=200)
	restaurant = models.ForeignKey(Restaurant)

	def __unicode__(self):
		return self.name


