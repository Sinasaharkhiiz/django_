from django.urls import include, path
from . import views
app_name = 'catalog'
urlpatterns = [
  path('', views.index.as_view() , name='index'),
  path('books/', views.BookListView.as_view() , name='books'),
  path('book/(?P<pk>\d+)',  views.BookDetailView.as_view(), name='book_detail'),
  path('authors/',  views.AuthorListView.as_view(), name='authors')
  ]
 
