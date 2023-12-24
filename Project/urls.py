from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('processing/',views.process_command,name='process_command'),
]
