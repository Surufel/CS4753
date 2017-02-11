# Sifer Aseph

from django.conf.urls import url

from lab1a.views import page

urlpatterns = [
    url(r'^$', page, name='page')
]
