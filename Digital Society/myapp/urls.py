from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('signup/',views.signup,name='signup'),
    path('index/',views.index,name='index'),
    path('member/',views.member,name="member"),
]