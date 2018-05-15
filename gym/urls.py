from django.conf.urls import url
from . import views

app_name = 'gym'
urlpatterns = [
    # /gym/
    url(r'^$', views.IndexView.as_view(), name="index"),
]
