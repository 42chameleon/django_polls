from django.db import models
import datetime
from django.contrib.auth.models import User


class Choice(models.Model):
    question = models.ForeignKey(
        'Question', related_name='choices', on_delete=models.CASCADE
    )
    text = models.CharField(max_length=75, default='Enter value')

    def __str__(self):
        return self.text

class Question(models.Model):

    class Type:
        TEXT = 'TEXT'
        CHOICE = 'CHOICE'
        MULTICHOICE = 'MULTICHOICE'

        choices = (
            (TEXT, 'TEXT'),
            (CHOICE, 'CHOICE'),
            (MULTICHOICE, 'MULTICHOICE'),
        )

    poll = models.ForeignKey('Poll', on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    type = models.CharField(
        max_length=11, choices=Type.choices, default=Type.TEXT
    )

    def __str__(self):
        return self.text

class Poll(models.Model):
    title = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.description

class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(default=datetime.date.today(), editable=False)

    def __str__(self):
        return self.poll.description

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    vote = models.ForeignKey(Vote, related_name='answers', on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    value = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.question.text
