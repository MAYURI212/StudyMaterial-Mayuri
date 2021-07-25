from django import forms
from django.db import models
from django.core.validators import FileExtensionValidator
from study_material.study_material_models.study_material_model import StudyMaterial
ch=(('pptx','PPT'),('pdf','PDF'),('docx','DOCX'))


class StudyMaterialForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'title','title':'Enter title'}),label='Your title ',max_length=10,min_length=2,required=True) 
    content_type=forms.ChoiceField(widget=forms.Select(attrs={'placeholder':'contenttype','title':'Select content type'}),choices=ch,label='content',required=True)
    upload=forms.FileField(validators=[FileExtensionValidator( ['pdf','pptx','docx'] ) ],label='Upload',required=True)
    #upload=forms.FileField(label='upload',validators=[FileExtensionValidator(['ppt','pdf','docx','mp4','mp3'])],required=True)
    subject=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'subject','title':'Enter subject'}),label='subject',max_length=10,min_length=2,required=True)
    class Meta:
        model=StudyMaterial
        fields=('title','content_type','upload','subject')