from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template import loader
from django.shortcuts import render

from .models import Question

# Create your views here.
def index(request):
    last_questuion = Question.objects.order_by('-pub_date')[:2]
    # template = loader.get_template('polls/resources/index.html')
    # context = {
    #     'last_question':last_questuion
    # }
    # return HttpResponse(template.render(context,request))
    return render(request,'polls/resources/index.html',{"last_questuion":last_questuion})