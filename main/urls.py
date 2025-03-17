from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('why/', views.why, name='why'),
    path('team/', views.team, name='team'),
    # path('signup/', views.signup, name='signup'),
    path('signup/', views.signup, name='signup'),  # New API endpoint for signup
    path('beneficiary/', views.beneficiary, name='beneficiary'),
]
