
from passapp import views
from django.urls import path,include


app_name='passapp'


urlpatterns=[

path('register/',views.register,name='register'),
path('user_login/',views.user_login,name='user_login'),


]
