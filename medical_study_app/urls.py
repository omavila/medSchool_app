from django.urls import path
from . import views

urlpatterns = [

path('', views.index, name='index'),
path('note_group/', views.NotegroupListView.as_view(), name= 'noteGroup'),
path('note_group/<int:pk>', views.NotegroupDetailView.as_view(), name= 'notegroup-detail'),
path('note_card/<int:pk>', views.NotecardDetailView.as_view(), name= 'notecard-detail'),
path('client/<int:pk>', views.ClientDetailView.as_view(), name= 'client-detail'),

path('client/<int:client_id>/create_notegroup/', views.createNotegroup, name='create_notegroup'),
path('client/<int:client_id>/delete_notegroup/<int:notegroup_id>/', views.deleteNotegroup, name='delete_notegroup'),
path('client/<int:client_id>/update_notegroup/<int:notegroup_id>/', views.updateNotegroup, name='update_notegroup'),
]
