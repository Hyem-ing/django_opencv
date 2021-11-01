from django import forms
from .models import ImageUploadModel

class SimpleUploadForm(forms.Form): # 파스칼 케이스

    title = forms.CharField(max_length=50)

    # file = forms.FileField()
    # 파일 업로드 받으려는 필드

    image = forms.ImageField()
    # FileField기능 포함

class ImageUploadForm(forms.ModelForm):

    class Meta:
        model = ImageUploadModel
        fields = ('description', 'document', )
        # fields 안에 있는거 문자열로 한다는게 중요

        
