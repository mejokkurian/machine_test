from pyexpat import model
from random import choices
from django.db import models

# Create your models here.

class quiz(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=100)
    
    def __str__(self):
        return self.question
 
    
class choices_and_answers(models.Model):
    question_id = models.ForeignKey(quiz,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    choices = models.CharField(max_length=50 )
    
    
    
    