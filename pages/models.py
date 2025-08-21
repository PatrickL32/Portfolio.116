from django.db import models

# Create your models here.

class skill(models.model):
    name = models.CharField(max_length=100)

    


class project(models.model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='prjects/')
    skills = models.ManyToManyField('skill')
    repository = models.URLField()


    def __str__(self):
        return f'{self.name} - {self.year}'