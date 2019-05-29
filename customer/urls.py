# from django.conf.urls import include, url
# import views

# urlpatterns = [
#     url(r'^login/', views.login),
#     url(r'^signup/', views.signup),
# ]
from django.urls import path

from . import views

urlpatterns = [

    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    
]