from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
    path('<int:pk>/',views.home, name='home'),
    
    path('',views.signin, name="signin"),
    path('signin',views.signin,name="signin"),
    path('signup',views.signup,name="signup"),
    path('signout',views.signout, name="signout"),

    path('createtask/<int:pk>/',views.createtask,name='createtask'),
    path('completed_tasks/<int:pk>/',views.completed_tasks,name="completed_tasks"),
    path('pending_tasks/<int:pk>/',views.pending_tasks,name="pending_tasks")
    
    
]
htmxpatterns=[
    path('update/<int:pk>/<int:pk1>/',views.update,name='update'),
    path('delete_task/<int:pk>/<int:pk1>',views.delete_task,name='delete_task')

]
urlpatterns += htmxpatterns