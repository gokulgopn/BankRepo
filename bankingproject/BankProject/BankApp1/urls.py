from django.urls import path
from . import views
app_name='BankApp1'
urlpatterns = [
    path('register',views.register,name='register'),
    path('new',views.new,name='new'),
    path('form',views.form,name='form'),
    path('final',views.final,name='final'),

]