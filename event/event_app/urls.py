from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create_event/', views.create_event, name="create_event"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('update_event/<int:id>', views.update_event, name="update_event"),
    path('delete_event/<int:id>', views.delete_event, name="delete_event"),
]
