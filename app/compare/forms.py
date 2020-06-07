from django import forms
from multiupload.fields import MultiFileField

class UploadFileForm(forms.Form):
    files = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        label = 'Upload your ride files.',
        help_text='Max 42 MB',
        # min_num=1,
        # max_num=10,
        # max_file_size=1024*1024*42
    )
