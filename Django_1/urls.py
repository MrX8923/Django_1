"""
URL configuration for Django_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path
from hello.views import index, about, contacts, month, product, contra, proverka

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('month/<str:ident>', month, name='month'),
    path('product/<str:num>', product, name='product'),
    path('list/', contra, name='contra'),
    # path('proverka/<int:year>', proverka),
    re_path(r'^about', about),
    re_path(r'^proverka/(?P<year>\d{4})', proverka),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""
r - регулярные выражения
^ - начало
$ - конец
| - "или"
(?P аргумет выражение)
"""