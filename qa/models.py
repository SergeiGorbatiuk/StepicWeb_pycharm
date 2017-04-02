from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-id')

    def popular(self):
        return self.order_by('-rating')

    def get_answers(self,question):
        return Answer.objects.filter(question = question)

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length = 255)
    text = models.TextField()
    added_at = models.DateTimeField(blank = True)
    rating = models.IntegerField(default = 0)
    author = models.ForeignKey(User, related_name = 'author')
    likes = models.ManyToManyField(User)

    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank = True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)