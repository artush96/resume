"""resume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

# from core.sitemaps import SitemapSkills


admin.site.site_header = "MyResume Admin"
admin.site.site_title = "MyResume Admin"
admin.site.index_title = "MyResume Admin"


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('sitemap.xml', SitemapSkills),
    path('sitemap.xml/', TemplateView.as_view(template_name="sitemap.xml", content_type='text/xml')),
    path('', include('core.urls')),
]



if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)