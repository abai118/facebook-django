from django.urls import path
from facebookapp import views
from django.conf import settings
from django.conf.urls.static import static


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

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
