from django.db import models

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    desc = models.TextField()

    def __str__(self):
        return self.name

class Teacher_details(models.Model):
    # Personal Details
    tid = models.AutoField(primary_key=True,null=False,editable=False)
    tname=models.CharField(max_length=122,null=True)
    temail=models.CharField(max_length=122,null=True)
    tphone=models.CharField(max_length=122,null=True)
    tdob=models.DateField(null=True)
    tadd=models.TextField()
    # Educational Details
    tsscs=models.CharField(max_length=122,null=True)
    tsscp=models.CharField(max_length=122,null=True)
    thscs=models.CharField(max_length=122,null=True)
    thscp=models.CharField(max_length=122,null=True)
    tgp=models.CharField(max_length=122,null=True)
    tgc=models.CharField(max_length=122,null=True)
    tpgp=models.CharField(max_length=122,null=True)
    tpgc=models.CharField(max_length=122,null=True)
    # Profesional Details
    tge=models.CharField(max_length=122,null=True)
    teq=models.CharField(max_length=122,null=True)
    teqy=models.CharField(max_length=122,null=True)
    teacher_service=models.CharField(max_length=122,null=True)
    join_date=models.DateField(null=True)
    teacher_salary=models.CharField(max_length=122,null=True)
    teacher_exp=models.CharField(max_length=122,null=True)
    field_name = models.FileField(blank="True",upload_to="media")
    

    def __str__(self):
        return self.tname

