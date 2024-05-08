from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView, NoteListCreate, NoteDelete
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.views import  TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/user/register/", CreateUserView.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),  # Use MyTokenObtainPairView
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api-auth/", include("rest_framework.urls")),
    # path("api/",include("api.urls")),
     path('api/notes/',NoteListCreate.as_view(),name='note-list'),
    path("api/notes/delete/<int:pk>/",NoteDelete.as_view(),name="delete-note"),
]