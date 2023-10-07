from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   path('accounts/', include('allauth.urls')),
   # Django скажет,
   # как обрабатывать запросы от пользователей по ссылкам,
   # которые начинаются с /accounts/.
   # path('accounts/', include('django.contrib.auth.urls')),
   # path('pages/', include('django.contrib.flatpages.urls')),
   # path('accounts/', include('accounts.urls')),
   # Делаем так, чтобы все адреса из нашего приложения (simpleapp/urls.py)
   # подключались к главному приложению с префиксом products/.
   path('products/', include('simpleapp.urls')),
]