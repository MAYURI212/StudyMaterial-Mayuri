from datetime import *
from django.shortcuts import redirect,render
from django.http import HttpResponse, HttpResponseRedirect
import xlwt
from xlwt.Formatting import Borders
from study_material.study_material_models.study_material_model import StudyMaterial



def fDesk_inward_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="InwardList.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('IList')
    # Sheet header, first row
    row_num = 0
    excel_style = xlwt.XFStyle()
    excel_style.font.bold = True
    borders = xlwt.Borders()
    borders.left = 1
    borders.right = 1
    borders.top = 1
    borders.bottom = 1
    excel_style.borders = borders
    columns = ["title","content_type","upload","subject",]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], excel_style)
    excel_style = xlwt.XFStyle()
    excel_style.borders = borders
    rows = StudyMaterial.objects.all().values_list('title','content_type','upload','subject',)
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
             ws.write(row_num, col_num, row[col_num], excel_style)
    wb.save(response)
    return response




def fDesk_inward_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="InwardList.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('IList')
    # Sheet header, first row
    row_num = 0
    excel_style = xlwt.XFStyle()
    excel_style.font.bold = True
    borders = xlwt.Borders()
    borders.left = 1
    borders.right = 1
    borders.top = 1
    borders.bottom = 1
    excel_style.borders = borders
    columns = ["Title","Content_type","Upload","Subject",]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], excel_style)
    excel_style = xlwt.XFStyle()
    excel_style.borders = borders
    rows = StudyMaterial.objects.all().values_list('title','content_type','upload','subject',)
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
             ws.write(row_num, col_num, row[col_num], excel_style)
    wb.save(response)
    return response
