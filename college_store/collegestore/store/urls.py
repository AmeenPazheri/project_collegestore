from . import views
from django.urls import path
app_name='store'
urlpatterns = [
    path('',views.index,name='index'),
    path('courses/',views.courses,name='courses'),
    path('new/',views.new,name='new'),
]
