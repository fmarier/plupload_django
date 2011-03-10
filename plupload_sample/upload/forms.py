from django import forms

class UploadForm(forms.Form):
    file = forms.FileField()

    def save(self, uploaded_file):
        print 'File "%s" would presumably be saved to disk now.' % uploaded_file.name
        pass
