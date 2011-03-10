from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'plupload_sample.upload.views.upload_file'),
)
