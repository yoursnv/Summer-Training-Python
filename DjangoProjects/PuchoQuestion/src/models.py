from django.db import models


class Question(models.Model):
	question_text = models.CharField(max_length = 150)
	date_published = models.DateTimeField('date published')

class Answer(models.Model):
	question = models.ForeignKey(Question)
	answer_text = models.CharField(max_length = 150)
	no_of_votes = models.IntegerField(default = 0)


