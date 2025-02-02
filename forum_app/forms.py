from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Message

class MessageForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Message
        fields = ['content',]