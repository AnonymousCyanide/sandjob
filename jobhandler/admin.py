from django.contrib import admin
from .models import (Job , JobCategory , Company , JobType)
# Register your models here.
admin.site.register(JobCategory)
admin.site.register(Job)
admin.site.register(Company)
admin.site.register(JobType)
