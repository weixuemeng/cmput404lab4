from django.db import models

# Create your models here.
# primary key is unique.
class Question(models.Model): # model.Model is build in so primary key is provided ( but could change)
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):  # 
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
