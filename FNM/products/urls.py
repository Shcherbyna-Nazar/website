from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
urlpatterns = [

    path('<int:id>',views.tank1, name='tank1'),
    path('cart', views.cart_show, name='cart'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)