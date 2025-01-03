from django.contrib import admin
from django.urls import path, include
from library.library_views import views


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('api/books/', views.BookListView.as_view(), name='book-list'),
    path('api/books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('api/recommendations/', views.RecommendationListView.as_view(), name='recommendations'),
    path('api/like/', views.LikeListView.as_view(), name='like'),
    path('api/saved/', views.SavedListView.as_view(), name='saved'),
    path('admin/add_book/', views.add_book, name='add_book'),
    path('admin/admin_book_list/', views.admin_book_list, name='admin_book_list'),
    path('admin/edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('admin/delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('admin/add_user/', views.add_user, name='add_user'),
    path('admin/user_list/', views.user_list, name='user_list'),
    path('admin/edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('admin/delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('library.library_models.urls')),
    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.sign_up, name='register'),
    path('library/<int:book_id>/like', views.like_book, name='like_book'),
    path('library/<int:book_id>/save', views.save_book, name='save_book'),
    path('library/like_list', views.like_book_list, name='like_book_list'),
    path('library/save_list', views.save_book_list, name='save_book_list'),
    path('accounts/change_username', views.change_username, name='change_username'),
]