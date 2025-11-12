from django.urls import path
from APIx import views
from APIx.views import accountApi

urlpatterns = [
     path('account', views.accountApi),
     path('account/<int:id>', accountApi, name='account_api'),
     path('account/', views.accountApi),
     path('account', views.accountApi),
]
