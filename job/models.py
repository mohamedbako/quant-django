from django.db import models
from django.utils.text import slugify

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
    JobResponsibilities = models.TextField(max_length=1000)
    JobRequirements = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=imageUpload) #this fun will create a new folder for images

    slug = models.SlugField(blank=True, null= True)


    def save(self,*args, **kwargs):
        self.slug = slugify(self.title) 
        super(Job, self).save(*args, **kwargs)




    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    


class ApplyReq(models.Model):
    job = models.ForeignKey(Job, verbose_name=("applyJob"), on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    age = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    location = models.CharField(max_length=100)
    cv = models.FileField(upload_to='apply/')
    linkedIn = models.URLField()
    cover = models.CharField(max_length=350)
    applied_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.firstName
    