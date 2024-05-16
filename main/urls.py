from django.urls import path
from .views import index, blog, docs, nnt, grant, oav, streets, BlogDetailView, GrantDetailView, OAVDetailView


urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('docs/', docs, name='docs'),
    path('nnt/', nnt, name='nnt'),
    path('grant/', grant, name='grant'),
    path('grant/<int:pk>/', GrantDetailView.as_view(), name='grant_detail'),
    path('oav/<int:pk>/', OAVDetailView.as_view(), name='oav_detail'),
    path('oav/', oav, name='oav'),
    path('streets/', streets, name='streets'),
]


