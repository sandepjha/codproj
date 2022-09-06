from xml.dom.minidom import Document
from django.urls import path
from .views import PostListView, PostDetailView, PostEditView, PostDeleteView, ProfileView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',PostListView.as_view(),name='post-list'),
    path('post/<int:pk>',PostDetailView.as_view(),name='post-detail'),
    path('post/edit/<int:pk>', PostEditView.as_view(),name='post-edit'),
    path('post/delete/<int:pk>',PostDeleteView.as_view(),name='post-delete'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)