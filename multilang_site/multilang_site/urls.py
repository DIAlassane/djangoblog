from django.contrib import admin
from django.urls import path
from main.views import ExtendedFront, switch_to_french, switch_to_english
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('', ExtendedFront, name='ExtendedFront'),
    path('admin/', admin.site.urls),
    path('fr/', switch_to_french, name='switch_to_french'),
    path('en/', switch_to_english, name='switch_to_english'),
)