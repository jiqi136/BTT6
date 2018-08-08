
from django.conf.urls import include, url
from . import views


app_name = '说明页'
urlpatterns = [
    url(r'^$', views.index, name='index'),

    # url(r'^question/', include('question.urls')),
# ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]