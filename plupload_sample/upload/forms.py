from django import forms

class UploadForm(forms.Form):
    file = forms.FileField()

    def save(self, temp_file, uploaded_file):
        print 'File "%s" would presumably be saved to disk now.' % uploaded_file
        pass
