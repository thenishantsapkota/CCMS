from django.urls import path

from web_app.views import CertificateSearchView, CertificateView, LandingView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("create/", CertificateView.as_view(), name="create"),
    path("search/", CertificateSearchView.as_view(), name="search"),
    path("", LandingView.as_view(), name="landing")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
