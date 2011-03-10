from django.conf.urls.defaults import *

from plupload_sample import settings

urlpatterns = patterns('',
    (r'^$', 'plupload_sample.upload.views.upload_file'),
    (r'^css/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '%s/static/css' % settings.PROJECT_ROOT}),
    (r'^js/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '%s/static/js' % settings.PROJECT_ROOT}),
)
