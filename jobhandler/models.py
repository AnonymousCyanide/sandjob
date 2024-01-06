from collections.abc import Iterable
from django.db import models
from .services import categories_count_update
# Create your models here.
class JobCategory(models.Model):
    code = models.CharField(max_length=10 , null=True , blank=True , unique=True)
    title = models.CharField(max_length=50)
    count = models.IntegerField(default=0)
    description = models.CharField(max_length=500)
    icon_code = models.CharField(max_length=50 , default='flaticon-content')

    def __str__(self) -> str:
        return str(self.code)+' - ' + str(self.title)
    
class Company(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10 , null=True , blank=True , unique=True)
    logo = models.ImageField(upload_to ='static/media/companylogo')
    website = models.URLField(max_length=200)

    def __str__(self) -> str:
        return str(self.code)+' - ' + str(self.name)
    
class JobType(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10 , unique=True)

    def __str__(self) -> str:
        return str(self.name) + ' - ' + str(self.code)
class Job(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=15, null=True , blank=True)
    description = models.CharField(max_length=500)
    url = models.URLField(max_length=200)
    type = models.ManyToManyField(JobType)
    category = models.ForeignKey(JobCategory , on_delete=models.SET_NULL , null=True , blank=True)
    company = models.ForeignKey(Company , on_delete=models.SET_NULL , null=True , blank=True)

    def __str__(self) -> str:
        return str(self.name) + ' - ' + str(self.category)
    
    def save(self, *args , **kwargs) -> None:
        categories_count_update(Job , JobCategory)
        return super().save(*args , **kwargs)
    
