from django.urls import path
from . import views

urlpatterns = [
    path('show/',views.showforms,),
    path('successfull/',views.success),
    path('suerform/',views.usercform,name='regestion'),
    path('logins/',views.login_form,name='logins'),
    path('successfull/',views.slogin,name='logins'),



]
