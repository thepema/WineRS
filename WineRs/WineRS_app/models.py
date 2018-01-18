# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Wine(models.Model):
	
	country = models.CharField(max_length=50)
	description = models.CharField(max_length=500)
	designation = models.CharField(max_length=50)
	points = models.CharField(max_length=10)
	price = models.IntegerField()
	province = models.CharField(max_length=50)
	region_1 = models.CharField(max_length=50)
	region_2 = models.CharField(max_length=50)
	variety = models.CharField(max_length=50)
	winery = models.CharField(max_length=50)
	def __init__(self):
		return self.designation
