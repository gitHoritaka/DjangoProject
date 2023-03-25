from django.urls import path
from . import views
urlpatterns = [
    #path('',views.taskList)#intial entry -> views.taskList(function)
    path('',views.Index.as_view(),name = 'news'),#root directory -> views.asviews(using class)
]
