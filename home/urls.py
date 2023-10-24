from django.urls import path
from .views import Newsapp,DetailPost,ModelUpdateView,DeletePost,CreatePost,formcontact
urlpatterns = [
    
    path('',Newsapp.as_view(),name='index'),
    path('blog/<int:pk>/',DetailPost.as_view(),name='blog'),
    path('update/<int:pk>/',ModelUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',DeletePost.as_view(),name='delete'),
    path('createpost/',CreatePost.as_view(),name='createpost'),
    path('contacts/',formcontact,name='contacts'),
    
 
]

