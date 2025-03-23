from django.urls import path
from . import views

urlpatterns = [
    path('', views.curd, name='curd'),
    path('post_create/', views.post_create, name='upload_post'),
    path('logout/', views.custom_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),

    # post list
    path('post_list/', views.post_list, name='post_list'),
    # delete page 
    path('post_list/delete/<int:post_id>/', views.delete_post, name='post_delete'),

    # edite page 
    path('post_list/edite/<int:post_id>/', views.edite_post, name='post_edite'),
    
    # comment details show 
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),

    # add comment 
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    # comment on reply 
    path('comment/<int:comment_id>/reply/', views.add_reply, name='add_reply'),

    path('contact/',views.contact,name='contact'),

    # search option invlable karta time 
    path('search/',views.search_results,name='search_results'),
    # about page
    path('about/',views.about,name='about'),
]
