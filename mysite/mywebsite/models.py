from django.db import models
# Create your models here.


class Introductions(models.Model):
    '''
    Each class represents a table in database
    Each object has methods to interact with the database
    - "save" for insert and update
    - "delete" for delete
    - "queries" to load records
    '''
    first = models.TextField(max_length=254)
    second = models.TextField(max_length=254)
    third = models.TextField(max_length=254)
