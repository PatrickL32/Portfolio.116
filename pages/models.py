from django.db import models

# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=100)

def __str__(self):
    return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='projects/')
    skills = models.ManyToManyField('Skill')
    repository = models.URLField()


    def __str__(self):
        return f'{self.name} - {self.year}'