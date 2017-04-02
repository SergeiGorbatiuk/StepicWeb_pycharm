from django.conf.urls import url
from qa import views

urlpatterns = [
    url(r'^(?P<q_id>\d+)/$', views.distinct_q, name='distinctQuestion')
]
