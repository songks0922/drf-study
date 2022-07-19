from django.db import models


class Book(models.Model):
    isbn = models.CharField("isbn", max_length=30)
    title = models.CharField("title", max_length=50)
    description = models.CharField('description', max_length=300)
    sell_count = models.IntegerField('sell_count')
    