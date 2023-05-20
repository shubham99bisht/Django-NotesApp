from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('update/<int:note_id>/', views.update_note, name='update'),
    path('delete/<int:note_id>/', views.delete_note, name='delete')
]