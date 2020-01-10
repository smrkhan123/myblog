from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('myblog/',views.myblog,name='myblog'),
    path('myaccount/',views.myaccount,name='myaccount'),
    path('addpost/',views.addpost,name='addpost'),
    path('viewblog/<id>',views.viewblog,name='viewblog'),
    path('delete/<id>',views.delete,name='delete'),
    path('edit/<id>',views.edit,name='edit'),
    path('likes/<id>',views.likes,name='likes'),
    path('comments/<id>',views.comments,name='comments'),
    path('entertainment/',views.entertainment,name='entertainment'),
    path('sports/',views.sports,name='sports'),
    path('travel/',views.travel,name='travel'),
    path('health/',views.health,name='health'),
    path('personal_life/',views.personal_life,name='personal_life'),
]