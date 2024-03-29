from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question,Choice

# Create your views here.
# def index(request):
#     last_questuion = Question.objects.order_by('-pub_date')[:2]
#     # template = loader.get_template('polls/resources/index.html')
#     # context = {
#     #     'last_question':last_questuion
#     # }
#     # return HttpResponse(template.render(context,request))
#     return render(request, 'polls/resources/index.html', {"last_questuion": last_questuion})
class indexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'last_questuion'
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:2]
        
# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("question does not found!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#     question=get_object_or_404(Question,pk=question_id)
#     return render(request, 'polls/resources/question.html', {"question": question})
class detailView(generic.DetailView):
    template_name = 'polls/question.html'
    model = Question
def vote(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/resources/index.html', {
            'question': question,
            'errorMessage':'do not vote',
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('index'))
