from django.urls import path

from library.library_views import views
from library.library_views.views import book_detail
from library.library_views.views import recommendations
from library.library_views.views import book_list

urlpatterns = [
    path('', book_list, name='book_list'),
    path('book_list', book_list, name='book_list'),
    path('book/<int:pk>/', book_detail, name='book_detail'),
    path('recommendations/', recommendations, name='recommendations'),
    path('library/<int:book_id>/like', views.like_book, name='like_book'),
    path('library/<int:book_id>/save', views.save_book, name='save_book'),
    path('library/like_list', views.like_book_list, name='like_book_list'),
    path('library/save_list', views.save_book_list, name='save_book_list'),
    path('accounts/change_username', views.change_username, name='change_username'),
    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.sign_up, name='register'),
]
