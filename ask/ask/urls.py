from django.conf.urls import  url

from django.contrib import admin
from django.contrib.auth.views import login
admin.autodiscover()
from qa.views import (
    test, new_questions, popular_questions, question_detail, ask, answer,
    signup)


urlpatterns = [
    url(r'^$',test),
    url(r'^new/$', test, name='new'),
    url(r'^popular/$', popular_questions, name='popular'),
    url(r'^ask/', ask, name='ask'),
    url(r'^answer/', answer, name='answer'),
    url(r'^question/(?P<question_id>[0-9]+)/$', question_detail,
        name='question_detail'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^$', new_questions, name='index'),
]