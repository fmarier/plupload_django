from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

from plupload_sample.upload.forms import UploadForm

@csrf_protect
def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            form.save(uploaded_file)

            return HttpResponseRedirect(reverse('plupload_sample.upload.views.upload_file'))
    else:
        form = UploadForm()

    return render_to_response('upload_file.html', {'form': form}, context_instance=RequestContext(request))
