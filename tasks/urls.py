from django.urls import path
from . import views 

urlpatterns = [
    path('', views.tasks , name="tasks"),
    path('form/', views.formtasks , name="addtasks"),
    path('form/delete/<int:id>/', views.delete , name="delete"),
    path('form/<int:id>/update/', views.update , name="update"),
]