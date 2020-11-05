from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('videojuego/<int:pk>', views.VideoJuegoDetailView.as_view(), name='videojuego-detail'),

]

urlpatterns+= [
    path('videojuego/create/', views.VideoJuegoCreate.as_view(), name='videojuego-create'),
    path('videojuego/<int:pk>/update/', views.VideoJuegoUpdate.as_view(), name='videojuego-update'),
    path('videojuego/<int:pk>/delete/', views.VideoJuegoDelete.as_view(), name='videojuego-delete'),
]