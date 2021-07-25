from django.urls import path
from study_material.study_material_views import add
from study_material.study_material_views import edit
from study_material.study_material_views import delete
from study_material.study_material_views import user_view
from study_material.study_material_views import export 


urlpatterns = [
    path('addpa',add.studyMaterial_Add,name='addpage'),
    path('<int:id>',edit.studyMaterial_edit,name='editpage'),
    path('delete/<int:id>',delete.studyMaterial_delete,name="deletepage"),
    path('usercreate',user_view.name,name='usercreate'),
    path('',user_view.login_view,name='login'),
    path('dash',user_view.dashboard_dash,name="dashboard"),
    path('logout',user_view.logout,name='logoutpage'),
    path('expire',user_view.pageExpir,name='pageExpirpage'),
    path('xport',export.fDesk_inward_xls,name='exportpage'),
    path('pdf',export.fDesk_inward_pdf,name='xport'),
    
    
]
