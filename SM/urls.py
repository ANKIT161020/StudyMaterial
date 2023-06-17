from django.urls import path
from . import views


urlpatterns =[
    path('index',views.home,name="home"),
    path('registration',views.registration,name='registration'),
    path('',views.registration,name='registration'),
    path('login',views.login_page,name='login_page'),
    path('Logout_page',views.LogoutPage,name="logout_page"),
    path('sem3',views.sem3,name="sem3"),
    path('sem4',views.sem4,name="sem4"),
    path('sem5',views.sem5,name="sem5"),
    path('sem6',views.sem6,name="sem6"),
    path('sem7',views.sem7,name="sem7"),
    path('sem8',views.sem8,name="sem8"),
    path('additem/',views.additem,name="additem"),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('contactus/',views.contactus,name='contactus'),
]
