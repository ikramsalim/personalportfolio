from django.db import models

# Create your models here.
#Install p
class Job(models.Model):
    #Images and summary
    image = models.ImageField(upload_to="images/")
    #summary is text hence will be charField
    summary= models.CharField(max_length=200)


    def __str__(self):
        return self.summary
