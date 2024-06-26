from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name ="home"),
    path('update_task/<str:pk>/',views.updateTask,name = "update_task"),
    path('delete_task/<str:pk>/',views.deleteTask,name = "delete_task"),
    path('register/',views.registerTask,name = "register"),
    path('login/',views.loginTask,name = "login"),
    path('logout/',views.logoutTask,name = "logout"),

]