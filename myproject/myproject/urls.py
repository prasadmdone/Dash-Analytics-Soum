"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include , url
from django.urls import path
from django.urls import reverse
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',include("webapp.urls")),
    path('utables/', include("webapp.urls")),
    path('userins/', include("webapp.urls")),
    path('impressions/', include("webapp.urls")),
    path('reaches/', include("webapp.urls")),
    path('genderdist/', include("webapp.urls")),

    path('HRlogmodel/', include("webapp.urls")),
    path('model/', include("webapp.urls")),
    path('sales/', include("webapp.urls")),
    path('', RedirectView.as_view(url='/sales/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
