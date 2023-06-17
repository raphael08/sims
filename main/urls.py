from django.urls import path
from . import views


urlpatterns = [
    path('',views.sensordata_table, name='dashboard'),
    path('post/<str:moisture>/<str:level>/<str:temperature>/<str:humidity>/', views.postData, name='post_url'),
]