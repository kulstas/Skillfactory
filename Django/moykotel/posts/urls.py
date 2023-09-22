from django.contrib import admin
from django.urls import path

# Импортируем созданное нами представление
# from .views import PostsList
#
urlpatterns = [
    path("admin/", admin.site.urls),
    # path("posts/", PostsList.as_view()),
]
