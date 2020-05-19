from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(
        label='Upload your ride file.',
        help_text='Max 42 megabytes'
    )