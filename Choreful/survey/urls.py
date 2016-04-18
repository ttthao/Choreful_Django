from django.conf.urls import url

from . import views

app_name = 'survey'
urlpatterns = [
    # /survey/
    #url(r'^$', views.index, name='index'),
    # /survey/5/
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # /survey/5/results
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    #/survey/5/vote
    url(r'^(?P<question_id>[0-9]+)/submit/$', views.submit, name='submit'),
]

