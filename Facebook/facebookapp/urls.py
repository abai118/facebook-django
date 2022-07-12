from django.urls import path
from facebookapp import views


urlpatterns = [
    path('',views.index,name='index'),
]
