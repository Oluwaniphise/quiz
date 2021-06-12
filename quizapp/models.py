from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    question_text = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    # score = models.IntegerField(default=0)
    answer = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text



class Score(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    

    # def __str__(self):
    #     return self.user

    