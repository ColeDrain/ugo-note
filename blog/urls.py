from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.PostListView.as_view(),
        name='home'
    ),
    path(
        '<slug:slug>/detail/',
        views.detail,
        name='detail'
    ),
    path(
        'about/',
        views.AboutView.as_view(),
        name='about'
    ),

    path('tag/<slug:tag_slug>/', views.tag_detail, name="tag_detail"),

    path('contact/', views.contact, name='contact'),
]