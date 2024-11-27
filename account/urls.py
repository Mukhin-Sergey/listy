from django.urls import path
from . import views

urlpatterns = [
    path('', views.account_view, name='account'),
    path('delete/<int:track_id>/', views.delete_view, name='delete'),
    path('logout/', views.logout_view, name='logout'),
]
