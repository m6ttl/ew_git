__author__ = '��ά�Ƽ�'


from django.conf.urls import url, include
from search import views

urlpatterns = [
    url(r'^search/', views.search, name='search'),
]


