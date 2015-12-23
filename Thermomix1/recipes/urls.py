'''
Created on 16 de dic. de 2015

@author: fjmora
'''
from django.conf.urls import patterns, include, url
from recipes import views

urlpatterns = patterns('recipes.views',
    url(r'^$', 'list', name='list'),
    url(r'^list/$', 'list', name='list'),
    url(r'^recipe/favorite_recipe/(?P<id>\d+)$', views.change_favorite_recipe),
)