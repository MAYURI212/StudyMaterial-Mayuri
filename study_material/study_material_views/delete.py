from django.shortcuts import render,redirect
from django.contrib import messages
from study_material.study_material_forms.study_material_form import StudyMaterialForm
from study_material.study_material_models.study_material_model import StudyMaterial

def studyMaterial_delete(request,id):
    if request.method=='POST':
        list_delete=StudyMaterial.objects.get(pk=id)
        list_delete.delete()
        messages.success(request,'File deleted sucessfully!')
        return redirect('addpage')