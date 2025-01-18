from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Comment

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Comment
        fields = ['body',]