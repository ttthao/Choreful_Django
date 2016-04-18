from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Answer

class IndexView(generic.ListView):
	template_name = 'survey/index.html'
	context_object_name = 'latest_question_list'
	
	def get_queryset(self):
		#return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
		return Question.objects.all()

class DetailView(generic.DetailView):
	model = Question
	template_name = 'survey/detail.html'
	def get_queryset(self):
		return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'survey/results.html'

#def index(request):
	#latest_question_list = Question.objects.order_by('-pub_date')[:5]
        #template = loader.get_template('survey/index.html')
	#context =  {'latest_question_list': latest_question_list,}
	#return render(request, 'survey/index.html', context)

#def detail(request, question_id):
	#question = get_object_or_404(Question, pk=question_id)
	#return render(request, 'survey/detail.html', {'question': question})

#def results(request, question_id):
	#question = get_object_or_404(Question, pk=question_id)
	#return render(request, 'survey/results.html', {'question': question})
def submit(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		answer = question.answer_set.get(pk=request.POST['choice'])
	except (KeyError, Answer.DoesNotExist):
		return render(request, 'survey/detail.html', {
			'question': question,
			'error_message': "You didn't submit a response.",
		})
	else:
		selected_answer.save()
		return HttpResponseRedirect(reverse('survey:results', args=(question.id,)))

