from django.conf.urls.static import static
from django.urls import path

from config import settings
from core.traceable.views import *

app_name = 'traceable'

urlpatterns = [
    path('add/', VegetalMaterialCreate.as_view(), name='material_create'),
    path('list/', VegetalMaterialListView.as_view(), name='material_list'),
    # path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    # path('update-password/<int:pk>/', UserPasswordUpdateView.as_view(), name='user_password_update'),
    # path('detail/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    # path('profile/<int:pk>/', MyProfileDetailView.as_view(), name='user_profile'),
    # path('profile/edit/<int:pk>/', ProfileUpdateView.as_view(), name='user_profile_update'),
    # path('edit/password/', UserChangePasswordView.as_view(), name='change_password'),
    # path('register/', registerview, name='account_create')
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)