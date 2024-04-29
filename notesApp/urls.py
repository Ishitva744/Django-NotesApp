from django.urls import path
from . import views

urlpatterns = [
	path('' , views.home , name = 'home'),
	path('mynotes/' , views.mynotes , name = 'mynotes'),
	path('mynotes/create', views.create , name = 'create'),
	path('mynotes/delete/<int:id>', views.delete , name = 'delete'),
	path('mynotes/update/<int:id>', views.update , name = 'update'),
]