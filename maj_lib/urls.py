from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
# from debug_toolbar.toolbar import debug_toolbar_urls
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    
    path('books/', include("books.urls")),
    path('take_book/', include("take_book.urls")),
    path('users/', include('users.urls')),
    path('rules/', TemplateView.as_view(template_name='rules.html'), name='rules'),
] # + debug_toolbar_urls()

urlpatterns += [re_path(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], serve, {'document_root': settings.MEDIA_ROOT})]