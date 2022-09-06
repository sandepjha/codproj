from django.urls import path
from cdpr import views

urlpatterns = [
    path('', views.base),
    path('signup/',views.Signup,name="signup"),
    path('login/',views.Login,name="login"),
    path('home/',views.home,name="home"),
    path('signout/',views.signout, name='signout')
]
