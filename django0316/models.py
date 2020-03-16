
# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Post(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()

    def __str__(self):
        return self.title

class University(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    date_birth = models.DateField()
    residencce = models.CharField(max_length=200)
    photo = models.ImageField(blank=True)
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    intro = models.TextField()