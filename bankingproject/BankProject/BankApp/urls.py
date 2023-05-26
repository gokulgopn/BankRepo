from django.urls import path
from . import views
app_name='BankApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('redirect_idukki',views.redirect_idukki,name='redirect_idukki'),
    path('redirect_kottayam',views.redirect_kottayam,name='redirect_kottayam'),
    path('redirect_malappuram',views.redirect_malappuram,name='redirect_malappuram'),
    path('redirect_palakkad',views.redirect_palakkad,name='redirect_palakkad'),
    path('redirect_kochi',views.redirect_kochi,name='redirect_kochi'),
    path('login',views.login,name='login'),


]
