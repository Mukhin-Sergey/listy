from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('delete/<int:track_id>/', views.delete_track, name='delete_track'),
    path('edit/<int:track_id>/', views.edit_track, name='edit_track'),
]
