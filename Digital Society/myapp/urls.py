from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('signup/',views.signup,name='signup'),
    path('index/',views.index,name='index'),
    path('member-index/',views.member_index,name='member-index'),
    path('chairman-index/',views.chairman_index,name='chairman-index'),
    path('watchman-index/',views.watchman_index,name='watchman-index'),
    path('member/',views.member,name="member"),
]