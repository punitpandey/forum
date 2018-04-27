from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from dashboard import views
urlpatterns = [
    url('^$',views.index,name='index'),
    url('success',views.submitQuery,name='success'),
    url('^response/(\d)',views.submitResponse,name='response'),
    url('^query/(\d)',views.queryDetail,name='detail'),
    url('^query$',views.add_query,name='query'),
    url('^signup$',views.signup,name='signup'),
]