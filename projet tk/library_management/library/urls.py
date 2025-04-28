from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-livre/', views.add_livre, name='add_livre'),
    path('delete-livre/<int:id>/', views.delete_livre, name='delete_livre'),
    path('modify-livre/<int:id>/', views.modify_livre, name='modify_livre'),
    path('add-member/', views.add_member, name='add_member'),
    path('delete-member/<int:id>/', views.delete_member, name='delete_member'),
    path('modify-member/<int:id>/', views.modify_member, name='modify_member'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]