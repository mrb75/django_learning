from django.urls import path

from . import views

from polls.models import Question

urlpatterns = [
    path('',views.index,name='index'),
]
