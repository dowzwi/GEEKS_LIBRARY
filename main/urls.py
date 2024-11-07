from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from main_page import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('about_me/', views.about_me),
    path('about_my_pets/', views.about_my_pets),
    path('datetime/', views.show_time),

]

urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                     document_root=settings.STATIC_ROOT)