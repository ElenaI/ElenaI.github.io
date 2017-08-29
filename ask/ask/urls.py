from django.conf.urls import url
from django.contrib import admin

admin.autodiscover()


urlpatterns = [
    url(r'^$', qa.views.test),
    url(r'^login/.*$', qa.views.test,name = 'login'),
    url(r'^signup/.*', qa.views.test,name = 'signup'),
    url(r'^question/(?P<id>[0-9]+)/$', qa.views.test,name = 'question'),
    url(r'^ask/.*', qa.views.test,name = 'ask'),
    url(r'^popular/.*', qa.views.test,name = 'popular'),
    url(r'^new/.*', qa.views.test,name = 'new'),
]

