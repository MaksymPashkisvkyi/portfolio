from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import index

from .views import MainPageView

urlpatterns = [
                  path('', index, name='home'),
                  # path('', MainPageView.as_view(), name='main'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
