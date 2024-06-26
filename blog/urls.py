from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blog.apps import BlogConfig
from blog.views import EditCreateView, EditListView, EditDetailView, EditUpdateView, EditDeleteView

app_name = BlogConfig.name

urlpatterns = ([
                   path('create/', EditCreateView.as_view(), name='create'),
                   path('', EditListView.as_view(), name='list'),
                   path('view/<int:pk>', EditDetailView.as_view(), name='view'),
                   path('edit/<int:pk>', EditUpdateView.as_view(), name='edit'),
                   path('delete/<int:pk>', EditDeleteView.as_view(), name='delete'),
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
