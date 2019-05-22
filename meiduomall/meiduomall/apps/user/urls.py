from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'meiduo', views.RegisterView.as_view())
]