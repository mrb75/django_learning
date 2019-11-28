from django.urls import path

from . import views

from polls.models import Question

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:question_id>', views.detail, name='detail'),
    path('vote/<int:question_id>',views.vote,name='vote'),
]
