#!/bin/python
# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class userInfo(models.Model):
    id = models.CharField(primary_key=True,max_length = 10)
    username = models.CharField(max_length = 24)
    sex = models.CharField(choices = (('M','男'),('F','女')),max_length = 10)
    info = models.TextField()
    timestamp = models.DateTimeField()
    
    