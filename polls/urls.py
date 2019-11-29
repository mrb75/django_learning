from django.urls import path

from . import views

from polls.models import Question

urlpatterns = [
    path('', views.indexView.as_view(), name='index'),
    path('detail/<int:pk>', views.detailView.as_view(), name='detail'),
    path('vote/<int:question_id>',views.vote,name='vote'),
]
