from django.urls import path
from django.views.i18n import JavaScriptCatalog

from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]
