from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question
#Выводит 5 последних вопросов
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'webexample/index.html', context)
#Ф-ция проверки на существования вопроса по id
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'webexample/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'webexample/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])#checks for KeyError and redisplays the question form with an error message if choice isn’t given.
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'webexample/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('webexample:results', args=(question.id,)))
# Create your views here.
