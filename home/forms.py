from django import forms  
from .models import Teacher_details 
class TeacherForm(forms.ModelForm):  
    class Meta:  
        model = Teacher_details
        fields = "__all__"  