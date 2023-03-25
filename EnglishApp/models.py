from django.db import models

# Create your models here.
class Word(models.Model):
    saved_word = models.CharField(max_length=20)
    word_value = models.IntegerField(default=0)
    word_count = models.IntegerField(default=0)
    added_date = models.DateTimeField(help_text='intial inserted date',auto_now_add=True)