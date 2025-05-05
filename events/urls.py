from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.event_list, name='list'),
    path('admin/list/', views.AdminEventListView.as_view(), name='admin_list'),
    path('admin/create/', views.EventCreateView.as_view(), name='create'),
    path('admin/edit/<int:pk>/', views.EventUpdateView.as_view(), name='edit'),
    path('admin/delete/<int:pk>/', views.EventDeleteView.as_view(), name='delete'),
]