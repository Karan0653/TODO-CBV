from django.urls import path, reverse_lazy 
from .views import TaskList,TaskDetail,TaskUpdate,TaskDelete,TaskCreate,CustomLogin,RegisterPage
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
    path('create/',TaskCreate.as_view(),name='create'),
    path('update/<int:pk>',TaskUpdate.as_view(),name='update'),
    path('delete/<int:pk>',TaskDelete.as_view(),name='delete'),
    path('login/',CustomLogin.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('register/',RegisterPage.as_view(), name='register')


]