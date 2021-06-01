from django.db import models

# Create your models here.
class Course(models.Model):
    course=models.CharField(max_length=200)
    language=models.CharField(max_length=100)
    platform=models.CharField(max_length=50)
    price=models.CharField(max_length=20)


    def __str__(self):
        return self.course+ '||'+ self.language+'||'+ self.platform+'||' +self.price