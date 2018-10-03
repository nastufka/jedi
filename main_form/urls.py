from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^jedi/$', views.jedi_form, name='jedi_form'),
    url(r'^candidate/$', views.candidate_form, name='candidate_form'),
    url(r'^test/$', views.test_form, name='test_form'),
    url(r'^list_candidate/$', views.candidate_on_planet, name='list_candidate'),
]
