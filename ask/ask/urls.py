from django.conf.urls import url
#from django.contrib import admin
from qa.views import test

#admin.autodiscover()
urlpatterns = [
    url(r'^$',test),
    url(r'^login/.*$',login, {'template_name': 'qa/login.html'}, name='login',name = 'login'),
    url(r'^signup/.*',signup, name = 'signup'),
    url(r'^question/(?P<id>[0-9]+)/$',question_detail,name = 'question_detail'),
    url(r'^ask/.*',ask,name = 'ask'),
    url(r'^popular/.*',popular_question,name = 'popular'),
    url(r'^new/.*', test,name = 'new'),
]

