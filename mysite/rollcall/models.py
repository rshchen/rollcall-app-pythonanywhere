from django.db import models

# Create your models here.

#name list entered by teacher       
class Teacher(models.Model):
	ClassroomId = models.TextField(blank=True)
	NameList = models.TextField(blank=True)
	def __str__(self):
        	return self.ClassroomId

        	
class StudentSignIn(models.Model):
	UserId = models.TextField(blank=True)
	ClassroomId = models.TextField(blank=True)
	name = models.TextField(blank=True)
	account = models.TextField(blank=True)
	def __str__(self):
        	return self.UserId
