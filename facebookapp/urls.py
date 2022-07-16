from django.urls import path
from facebookapp import views


urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login1,name='login'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    path('profile',views.profile,name='profile'),
    path('updateProfile',views.updateProfile,name='updateProfile'),
    path('friends',views.friends,name='friends'),
    path('updatePost',views.updatePost,name='updatePost')
   
    

]
