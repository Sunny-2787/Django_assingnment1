
from django.contrib import admin
from django.urls import path,include
from core.views import home,no
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("Tasks/",include("Tasks.urls")),
    path("users/",include("users.url")),
    path("",home,name='home'),
    path("no-permission",no,name='no-permission')

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)