from django.shortcuts import render,redirect
from study_material.study_material_forms.study_material_form import StudyMaterialForm
from study_material.study_material_models.study_material_model import StudyMaterial
from django.contrib import messages



def studyMaterial_edit(request,id):
    if request.session.has_key('username'):
         lname=request.user.first_name 
         fname=request.user.last_name
         if request.method=='POST':
             UI=StudyMaterial.objects.get(pk=id)
             file_obj=StudyMaterialForm(request.POST,request.FILES,instance=UI)
             if file_obj.is_valid():
                 try:
                     file_obj.save()
                     messages.success(request,'File uploaded sucessfully!')
                     return redirect('addpage')
                 except:
                     messages.error(request,"Check your Internet connection... Try again")
                     return redirect('addpage')
             else:
                 messages.error(request,"Form is not valid")
         else:
             UI=StudyMaterial.objects.get(pk=id)
             file_obj=StudyMaterialForm(instance=UI)
         obj=StudyMaterial.objects.all()
         context={'file_obj':file_obj,'obj':obj,}
         return render(request,"webpages/add.html",context)
    else:
        return redirect('login')