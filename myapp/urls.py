from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name='index'),
    path('category/<str:id>',views.category,name='category'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('post_image/',views.post_image,name='post_image'),
    path('profile/',views.profile,name='profile'),
    path('delete/<int:id>',views.delete,name='delete')


]