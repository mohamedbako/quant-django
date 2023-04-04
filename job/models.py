from django.db import models


JOBTYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)

def imageUpload(instance, filename):
    imagename , extension = filename.split(".")
    return "postImages/%s.%s"%(instance.id, extension) 


# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    #location
    job_type = models.CharField(max_length=20, choices= JOBTYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=imageUpload) #this fun will create a new folder for images

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    