from django.urls import path
from .views import ListSectionView, ListSectionDetailView

urlpatterns = [
    path("section/", ListSectionView.as_view(), name="sections-all"),
    path("<int:pk>/", ListSectionDetailView.as_view(), name="section_detail"),
#    path('login/', LoginView.as_view(), name="auth-login"),
#    path('register/', RegisterUsers.as_view(), name="auth-register")
]
