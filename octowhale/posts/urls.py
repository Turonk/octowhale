from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [

    path('', views.PostsList.as_view(), name='index'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),

]