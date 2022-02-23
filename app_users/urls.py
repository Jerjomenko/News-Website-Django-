from django.urls import path
from .views import MainListView, RegistrationView, OutView, AuthView, ProfileView, UpdateUserView, NewsView, NewsDetailView

urlpatterns = [
    path("", MainListView.as_view(), name="index"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("logout/", OutView.as_view(), name="logout"),
    path("login/", AuthView.as_view(), name="login"),
    path("profile/<int:pk>/", ProfileView.as_view(), name="profile"),
    path("update_user/<int:pk>/", UpdateUserView.as_view(), name="update_user"),
    path("newscreate/<int:pk>/", NewsView.as_view(), name="newscreate"),
    path("detail/<int:pk>/", NewsDetailView.as_view(), name="detail")
]


