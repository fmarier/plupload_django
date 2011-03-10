from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
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
            chunk = request.REQUEST.get('chunk', '0')
            chunks = request.REQUEST.get('chunks', '0')
            name = request.REQUEST.get('name', '')

            if not name:
                name = uploaded_file.name

            temp_file = '/tmp/insecure.tmp'
            with open(temp_file, ('wb' if chunk == '0' else 'ab')) as f:
                for content in uploaded_file.chunks():
                    f.write(content)

            if int(chunk) + 1 >= int(chunks):
                form.save(temp_file, name)

            if request.is_ajax():
                response = HttpResponse('{"jsonrpc" : "2.0", "result" : null, "id" : "id"}', mimetype='text/plain; charset=UTF-8')
                response['Expires'] = 'Mon, 1 Jan 2000 01:00:00 GMT'
                response['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
                response['Pragma'] = 'no-cache'
                return response
            else:
                return HttpResponseRedirect(reverse('plupload_sample.upload.views.upload_file'))
    else:
        form = UploadForm()

    return render_to_response('upload_file.html', {'form': form}, context_instance=RequestContext(request))
