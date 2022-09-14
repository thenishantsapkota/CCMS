from django.urls import path
from web_app.views.authentication_views import (
    EditProfileView,
    LoginView,
    LogoutView,
    ProfileView,
)

from web_app.views.certificate_views import (
    CertificateSearchView,
    CertificateView,
    LandingView,
)

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path(
        "create/",
        login_required(CertificateView.as_view(), login_url="/login"),
        name="create",
    ),
    path(
        "search/",
        login_required(CertificateSearchView.as_view(), login_url="/login"),
        name="search",
    ),
    path("", login_required(LandingView.as_view(), login_url="/login"), name="landing"),
    path(
        "profile/",
        login_required(ProfileView.as_view(), login_url="/login"),
        name="profile",
    ),
    path(
        "edit-profile/",
        login_required(EditProfileView.as_view(), login_url="/login"),
        name="edit-profile",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
