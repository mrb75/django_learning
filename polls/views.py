from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

# Create your views here.
def index(request, *args, **kwargs):
    last_questuion=Question.objects.order_by
    return HttpResponse()