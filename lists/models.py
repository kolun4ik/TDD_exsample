from django.db import models
from django.core.urlresolvers import reverse



class List(models.Model):
    """список задач To-Do"""
    def get_absolute_url(self):
        """получить абсолютный Url"""
        return reverse('view_list', args=[self.id])

class Item(models.Model):
    """элемент списка"""
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)

    class Meta:
        ordering = ('id',)
        unique_together = ('list', 'text')

    def __str__(self):
        return self.text
