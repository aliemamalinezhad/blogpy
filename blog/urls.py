from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('contact/', views.ContactPage.as_view(), name='contact'),

    path('article/', views.SingleArticleApiView.as_view(), name='single_article'),
    path('article/all/', views.AllArticleApiView.as_view(), name='all_articles'),
    path('article/search/', views.SearchArticleApiView.as_view(), name='search_article'),
    path('article/submit/', views.SubmitArticleApiView.as_view(), name='submit_article'),
    path('article/update-cover/', views.UpdateArticleApiView.as_view(), name='update_article'),
    path('article/delete/', views.DeleteArticleApiView.as_view(), name='delete_article'),


]