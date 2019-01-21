
from django.urls import path
from blog_before import views

urlpatterns = [
    path('index/', views.index,name='index'),
    path('about/',views.about,name='about'),
    path('time/',views.time,name='time'),
    path('info/<int:id>/',views.info,name='info'),
    # path('life/',views.life,name='life'),
]
