from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='home_page'),
    path('login',views.login,name='login'),
    path('registration',views.registration,name='registration'),
    path('about',views.about,name='about'),
    path('contact1',views.contact,name='contact'),
    path('worker',views.worker,name='worker'),
    path('add_member',views.add_member,name='add_member'),
    path('logout',views.logout,name='logout'),
    path('<int:service_id>',views.service_provider,name='detail'),
]
