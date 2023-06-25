from django.urls import path
from .import views 

urlpatterns=[
	path('',views.index, name='index'),
	path('artist-index',views.artist_index,name='artist-index'),
	path('about/',views.about,name='about'),
	path('artist-about-us/',views.artist_about_us,name='artist-about-us'),
	path('contact/',views.contact, name='contact'),
	path('artist/',views.artist, name='artist'),
	path('login/',views.login,name='login'),
	path('signup/',views.signup,name='signup'),
	path('logout/',views.logout,name='logout'),
	path('profile/',views.profile,name='profile'),
	path('signup-artist/',views.signup_artist,name='signup-artist'),
	path('artist-change-password/',views.artist_change_password,name='artist-change-password'),
	path('forgot-password/',views.forgot_password,name='forgot-password'),
	path('verify-otp/',views.verify_otp,name='verify-otp'),
	path('new-password/',views.new_password,name='new-password')
]