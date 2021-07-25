from django.db import models

class StudyMaterial(models.Model):
    title=models.CharField(max_length=50,null=True)
    content_type=models.CharField(max_length=50,null=True)
    upload=models.FileField(upload_to='uploads',null=True)
    subject=models.CharField(max_length=50,null=True)
    

    
    