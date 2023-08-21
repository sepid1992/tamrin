

from django.urls import path
from news.views import *

urlpatterns = [
    
    path('',home),
    path('<adad>',entrancenews)
]

