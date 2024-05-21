from django.urls import path, include
from .views import home, auth_view, add_url, page_detail

urlpatterns = [
    path('signup/', auth_view, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home, name='home'),
    path('add/', add_url, name='add_url'),
    path('page/<int:page_id>/', page_detail, name='page_detail'),
]
