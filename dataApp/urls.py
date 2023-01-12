from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index),
    path('create',views.create),
    path('retrieve',views.retrieve),
    path('delete/<int:id>',views.delete,name="del"),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('form',views.entryForm),
    path('form1',views.dbForm),



    
]
