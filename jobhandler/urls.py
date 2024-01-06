from django.urls import path
from .views import( job_listing )
urlpatterns = [
    path('listing/', job_listing ,name='job_listing'),
   
]