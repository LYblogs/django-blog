from django.urls import path

from blog_back import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('article/', views.article, name='article'),
    path('category/', views.category, name='category'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('add_article/', views.add_article, name='add_article'),
    path('del_category/<int:id>/', views.del_category, name='del_category'),
    path('update_category/<int:id>/', views.update_category, name='update_category'),
    path('del_article/', views.del_article, name='del_article'),
    path('update_article/<int:id>/', views.update_article, name='update_article'),
]
