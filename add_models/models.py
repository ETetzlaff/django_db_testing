from django.db import models

# Create your models here.

class Stage_Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Stage_Choice(models.Model):
    poll = models.ForeignKey(Stage_Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
