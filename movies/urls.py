from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.add_movie, name='add_movie'),
    path('review/<slug:slug>/<int:_id>/', views.movie_review_page, name='review'),
    path('update/<slug:movie_slug>/<int:movie_id>/', views.update_movie, name='update_movie'),
    path('comment/update/<int:comment_id>/', views.update_comment, name='update_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]