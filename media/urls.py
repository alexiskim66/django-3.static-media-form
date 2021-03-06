from django.contrib import admin
from django.urls import path, include
from blog.views import home
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.media import media

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('blog/', include('blog.urls')),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)