from django.db import models

class student(models.Model):
    name = models.CharField(max_length=20)
    rno = models.CharField(max_length=20)
    def __str__(self):
        return self.name
